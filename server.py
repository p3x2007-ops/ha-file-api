#!/usr/bin/env python3
"""
File API Server for Home Assistant (v2.1 - full access)
Full filesystem access with Bearer token authentication
"""
import os
import json
import logging
import requests
from pathlib import Path
from flask import Flask, request, jsonify
from flask_cors import CORS
from functools import wraps

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

ALLOWED_BASES = ["/config", "/share", "/media", "/addons", "/backup", "/ssl", "/data"]
MAX_FILE_SIZE = 50 * 1024 * 1024
HA_API_URL = os.environ.get('HA_API_URL', 'http://supervisor/core/api')

OPTIONS_FILE = "/data/options.json"
API_SECRET = ""
AUTH_MODE = "home_assistant"

if os.path.exists(OPTIONS_FILE):
    with open(OPTIONS_FILE, 'r') as f:
        options = json.load(f)
        log_level = options.get('log_level', 'info').upper()
        logger.setLevel(getattr(logging, log_level))
        MAX_FILE_SIZE = options.get('max_file_size_mb', 50) * 1024 * 1024
        ALLOWED_EXTENSIONS = set(options.get('allowed_extensions', []))
        API_SECRET = options.get('api_secret', '')
        AUTH_MODE = options.get('auth_mode', 'home_assistant')
else:
    ALLOWED_EXTENSIONS = {'.yaml', '.yml', '.json', '.js', '.py', '.md', '.txt', '.sh', '.db', '.log', '.conf'}

def verify_api_secret(token):
    """Verify API secret token"""
    if not API_SECRET:
        return False
    return token == API_SECRET

def verify_ha_token(token):
    """Verify Home Assistant Bearer token"""
    try:
        response = requests.get(
            f"{HA_API_URL}/",
            headers={"Authorization": f"Bearer {token}"},
            timeout=5
        )
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Token verification error: {e}")
        return False

def verify_token(token):
    """Verify token based on auth mode"""
    if AUTH_MODE == "api_secret":
        return verify_api_secret(token)
    elif AUTH_MODE == "home_assistant":
        return verify_ha_token(token)
    elif AUTH_MODE == "both":
        return verify_api_secret(token) or verify_ha_token(token)
    return False

def require_auth(f):
    """Decorator to require authentication"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            logger.warning("Missing Authorization header")
            return jsonify({"error": "Missing Authorization header"}), 401

        if not auth_header.startswith('Bearer '):
            logger.warning("Invalid Authorization header format")
            return jsonify({"error": "Invalid Authorization header format"}), 401

        token = auth_header.replace('Bearer ', '', 1)
        if not verify_token(token):
            logger.warning(f"Invalid token: {token[:20]}...")
            return jsonify({"error": "Invalid or expired token"}), 401

        return f(*args, **kwargs)
    return decorated_function

def is_allowed_file(path):
    """Check if file extension is allowed"""
    ext = os.path.splitext(path)[1].lower()
    return ext in ALLOWED_EXTENSIONS

def safe_path(relative_path):
    """Convert path to safe absolute path within allowed bases"""
    relative_path = relative_path.lstrip('/')

    # Check if path starts with a known base directory
    for base in ALLOWED_BASES:
        base_name = base.lstrip('/')
        if relative_path.startswith(base_name + '/') or relative_path == base_name:
            full_path = os.path.normpath('/' + relative_path)
            if full_path.startswith(base) or full_path == base:
                return full_path

    # Default: resolve relative to /config
    full_path = os.path.normpath(os.path.join("/config", relative_path))
    if not any(full_path.startswith(base) for base in ALLOWED_BASES):
        raise ValueError(f"Path outside allowed bases: {ALLOWED_BASES}")

    return full_path

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint (no auth required)"""
    return jsonify({
        "status": "healthy",
        "version": "2.1.0",
        "full_access": True,
        "allowed_bases": ALLOWED_BASES,
        "auth_mode": AUTH_MODE,
        "api_secret_configured": bool(API_SECRET)
    })

@app.route('/api/file/read', methods=['POST'])
@require_auth
def read_file():
    """Read file content"""
    try:
        data = request.json
        if not data or 'path' not in data:
            return jsonify({"error": "Missing 'path' parameter"}), 400

        path = safe_path(data['path'])

        if not os.path.exists(path):
            return jsonify({"error": "File not found"}), 404

        if not os.path.isfile(path):
            return jsonify({"error": "Path is not a file"}), 400

        # Check file size
        file_size = os.path.getsize(path)
        if file_size > MAX_FILE_SIZE:
            return jsonify({"error": f"File too large (max {MAX_FILE_SIZE // 1024 // 1024} MB)"}), 413

        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

        logger.info(f"Read file: {data['path']} ({file_size} bytes)")
        return jsonify({
            "success": True,
            "path": data['path'],
            "content": content,
            "size": file_size
        })

    except ValueError as e:
        logger.warning(f"Security error: {e}")
        return jsonify({"error": str(e)}), 403
    except Exception as e:
        logger.error(f"Error reading file: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/file/write', methods=['POST'])
@require_auth
def write_file():
    """Write file content"""
    try:
        data = request.json
        if not data or 'path' not in data or 'content' not in data:
            return jsonify({"error": "Missing 'path' or 'content' parameter"}), 400

        path = safe_path(data['path'])
        content = data['content']

        # Check extension
        if not is_allowed_file(path):
            return jsonify({"error": f"File extension not allowed. Allowed: {list(ALLOWED_EXTENSIONS)}"}), 403

        # Check content size
        content_size = len(content.encode('utf-8'))
        if content_size > MAX_FILE_SIZE:
            return jsonify({"error": f"Content too large (max {MAX_FILE_SIZE // 1024 // 1024} MB)"}), 413

        # Create parent directory if needed
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Write file
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

        logger.info(f"Wrote file: {data['path']} ({content_size} bytes)")
        return jsonify({
            "success": True,
            "path": data['path'],
            "size": content_size
        })

    except ValueError as e:
        logger.warning(f"Security error: {e}")
        return jsonify({"error": str(e)}), 403
    except Exception as e:
        logger.error(f"Error writing file: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/file/delete', methods=['POST'])
@require_auth
def delete_file():
    """Delete a file"""
    try:
        data = request.json
        if not data or 'path' not in data:
            return jsonify({"error": "Missing 'path' parameter"}), 400

        path = safe_path(data['path'])

        if not os.path.exists(path):
            return jsonify({"error": "File not found"}), 404

        if not os.path.isfile(path):
            return jsonify({"error": "Path is not a file"}), 400

        os.remove(path)

        logger.info(f"Deleted file: {data['path']}")
        return jsonify({
            "success": True,
            "path": data['path']
        })

    except ValueError as e:
        logger.warning(f"Security error: {e}")
        return jsonify({"error": str(e)}), 403
    except Exception as e:
        logger.error(f"Error deleting file: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/file/list', methods=['POST'])
@require_auth
def list_files():
    """List files in a directory"""
    try:
        data = request.json or {}
        dir_path = data.get('path', '/')

        path = safe_path(dir_path)

        if not os.path.exists(path):
            return jsonify({"error": "Directory not found"}), 404

        if not os.path.isdir(path):
            return jsonify({"error": "Path is not a directory"}), 400

        files = []
        for item in sorted(os.listdir(path)):
            item_path = os.path.join(path, item)
            try:
                stat = os.stat(item_path)
                files.append({
                    "name": item,
                    "is_dir": os.path.isdir(item_path),
                    "size": stat.st_size if os.path.isfile(item_path) else 0,
                    "modified": int(stat.st_mtime)
                })
            except Exception as e:
                logger.warning(f"Error stating {item}: {e}")
                continue

        logger.info(f"Listed directory: {dir_path} ({len(files)} items)")
        return jsonify({
            "success": True,
            "path": dir_path,
            "files": files
        })

    except ValueError as e:
        logger.warning(f"Security error: {e}")
        return jsonify({"error": str(e)}), 403
    except Exception as e:
        logger.error(f"Error listing directory: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/file/exists', methods=['POST'])
@require_auth
def file_exists():
    """Check if file exists"""
    try:
        data = request.json
        if not data or 'path' not in data:
            return jsonify({"error": "Missing 'path' parameter"}), 400

        path = safe_path(data['path'])
        exists = os.path.exists(path)
        is_file = os.path.isfile(path) if exists else False
        is_dir = os.path.isdir(path) if exists else False

        return jsonify({
            "success": True,
            "path": data['path'],
            "exists": exists,
            "is_file": is_file,
            "is_dir": is_dir
        })

    except ValueError as e:
        logger.warning(f"Security error: {e}")
        return jsonify({"error": str(e)}), 403
    except Exception as e:
        logger.error(f"Error checking file: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/file/find', methods=['POST'])
@require_auth
def find_files():
    """Search for files by name pattern across all allowed bases"""
    try:
        data = request.json
        if not data or 'pattern' not in data:
            return jsonify({"error": "Missing 'pattern' parameter"}), 400

        search_path = safe_path(data.get('path', '/config'))
        pattern = data['pattern'].lower()
        max_results = min(data.get('max_results', 50), 200)

        results = []
        for root, dirs, files in os.walk(search_path):
            for name in files + dirs:
                if pattern in name.lower():
                    full = os.path.join(root, name)
                    results.append({"path": full, "is_dir": os.path.isdir(full)})
                    if len(results) >= max_results:
                        break
            if len(results) >= max_results:
                break

        logger.info(f"Find '{pattern}' in {search_path}: {len(results)} results")
        return jsonify({"success": True, "pattern": data['pattern'], "results": results, "count": len(results)})

    except ValueError as e:
        return jsonify({"error": str(e)}), 403
    except Exception as e:
        logger.error(f"Error finding files: {e}")
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    logger.info(f"Starting File API Server v2.1.0 - Full Access")
    logger.info(f"Allowed bases: {ALLOWED_BASES}")
    logger.info(f"Max file size: {MAX_FILE_SIZE // 1024 // 1024} MB")
    logger.info(f"Allowed extensions: {ALLOWED_EXTENSIONS}")
    logger.info(f"Authentication mode: {AUTH_MODE}")

    if AUTH_MODE in ("api_secret", "both"):
        if API_SECRET:
            logger.info(f"API Secret configured: {API_SECRET[:10]}...")
        else:
            logger.warning("API Secret NOT configured! Set 'api_secret' in addon configuration.")

    if AUTH_MODE in ("home_assistant", "both"):
        logger.info(f"HA API URL: {HA_API_URL}")

    app.run(
        host='0.0.0.0',
        port=8098,
        debug=False
    )
