# Configuration File API v2

## 🔐 Authentication Modes

File API v2 offers **3 configurable authentication modes** during installation.

### Mode 1: Home Assistant Token (Default)

**Configuration:**
```yaml
auth_mode: home_assistant
api_secret: ""  # Leave empty
```

**Usage:**
```bash
# Generate a Long-Lived Access Token in HA
# Profile → Long-lived access tokens → Create token

curl -X POST "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/read" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{"path": "configuration.yaml"}'
```

**✅ Advantages:**
- Maximum security (native HA token)
- Easy revocation in HA
- Expires if set

**❌ Disadvantages:**
- Long and complex token
- Requires regeneration if revoked

---

### Mode 2: Custom API Secret (Recommended for Claude)

**Configuration:**
```yaml
auth_mode: api_secret
api_secret: "my_super_secure_secret_123"  # Define your secret
```

**Usage:**
```bash
# Use your secret as Bearer token
curl -X POST "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/read" \
  -H "Authorization: Bearer my_super_secure_secret_123" \
  -H "Content-Type: application/json" \
  -d '{"path": "configuration.yaml"}'
```

**✅ Advantages:**
- Simple and memorable token
- No HA dependency
- Perfect for automated scripts

**❌ Disadvantages:**
- Less secure than an HA token
- No easy revocation (modify addon config)

**💡 Recommendation:** 
Generate a strong random secret:
```bash
# Generate a 32-character secret
openssl rand -base64 32 | tr -d "=+/" | cut -c1-32
# Ex: K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA
```

---

### Mode 3: Both

**Configuration:**
```yaml
auth_mode: both
api_secret: "my_secret_123"
```

**Usage:**
Accepts **either** HA token **or** your API secret.

**✅ Advantages:**
- Maximum flexibility
- HA token for occasional use
- API secret for automation

**❌ Disadvantages:**
- Larger attack surface
- More complex configuration

---

## ⚙️ Complete Configuration

### Add-on interface (after installation)

1. **Settings → Add-ons → File API v2**
2. **Configuration** tab
3. Modify values:

```yaml
# Authentication mode
auth_mode: api_secret  # home_assistant | api_secret | both

# API secret (if api_secret or both mode)
api_secret: "YOUR_SECRET_HERE"

# Log level
log_level: info  # debug, info, warning, error

# Allowed extensions
allowed_extensions:
  - .yaml
  - .yml
  - .json
  - .js
  - .py
  - .md
  - .txt
  - .sh

# Max file size (MB)
max_file_size_mb: 10
```

4. **Save**
5. **Restart the add-on**

---

## 🚀 Configured Installation Guide

### Step 1: Install the add-on

(Follow INSTALL.md)

### Step 2: Configure authentication

**For use with Claude Code (recommended):**

1. Open add-on configuration
2. Set:
   ```yaml
   auth_mode: api_secret
   api_secret: "K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA"  # Generate your own!
   ```
3. Save and restart

**For use with Home Assistant scripts:**

1. Leave default config:
   ```yaml
   auth_mode: home_assistant
   api_secret: ""
   ```
2. Create an HA token: **Profile → Long-lived access tokens**

### Step 3: Test

```bash
# Health check (see configured mode)
curl -s "${HA_URL}/api/hassio/ingress/file_api_v2/health"

# Result:
{
  "status": "healthy",
  "version": "2.0.0",
  "auth_mode": "api_secret",
  "api_secret_configured": true
}
```

```bash
# Test with your secret
curl -s -X POST "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/list" \
  -H "Authorization: Bearer K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA" \
  -H "Content-Type: application/json" \
  -d '{"path": "www"}'
```

---

## 🔒 Security

### Best Practices

**✅ DO:**
- Use a strong secret (32+ random characters)
- Never share your secret
- Change secret regularly
- Use HTTPS (Nabu Casa or reverse proxy)
- Limit network access to the add-on

**❌ DON'T:**
- Simple secret like "password123"
- Commit secret to Git
- Use the same secret everywhere
- Expose add-on on Internet without HTTPS

### Generate a Strong Secret

**Option 1: OpenSSL (Mac/Linux Terminal)**
```bash
openssl rand -base64 32 | tr -d "=+/" | cut -c1-32
```

**Option 2: Python**
```python
import secrets
print(secrets.token_urlsafe(32))
```

**Option 3: Website (if you don't have terminal access)**
https://passwordsgenerator.net/ (32 characters, alphanumeric)

---

## 📊 Mode Comparison

| Criteria | Home Assistant | API Secret | Both |
|----------|----------------|------------|------|
| Security | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Setup simplicity | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Automation | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Revocation | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |

**Recommendation by use case:**

| Usage | Recommended mode |
|-------|------------------|
| Automated Claude Code | `api_secret` |
| Occasional HA scripts | `home_assistant` |
| Shared environment | `home_assistant` |
| CI/CD pipelines | `api_secret` |
| Maximum security | `home_assistant` |
| Maximum simplicity | `api_secret` |

---

## 🐛 Troubleshooting

### Error: HTTP 401 "Invalid or expired token"

**Cause:** Incorrect token or misconfigured auth mode.

**Solution:**
1. Check mode: `curl ${HA_URL}/api/hassio/ingress/file_api_v2/health`
2. If `auth_mode: api_secret` → Use your secret
3. If `auth_mode: home_assistant` → Use HA token
4. Verify `api_secret_configured: true` if api_secret mode

### Error: "API Secret NOT configured"

**Cause:** Mode `api_secret` but empty field.

**Solution:**
1. Open add-on configuration
2. Fill `api_secret: "your_secret"`
3. Save and restart

### HA token no longer works

**Cause:** Token revoked or expired.

**Solution:**
1. HA Profile → Long-lived access tokens
2. Delete old token
3. Create new token
4. Update your scripts

---

## 💡 Usage Examples

### With Claude Code

1. Configure `api_secret` in the add-on
2. Save the secret in Claude's memory:

```bash
# In a conversation with Claude:
"My File API secret is: K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA"
```

3. Claude can then automate:
```bash
curl -X POST "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/write" \
  -H "Authorization: Bearer K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA" \
  -H "Content-Type: application/json" \
  -d '{"path": "www/dolce-gusto-card.js", "content": "..."}'
```

### With Node.js scripts

```javascript
const axios = require('axios');

const fileAPI = axios.create({
  baseURL: 'https://YOUR_INSTANCE.ui.nabu.casa/api/hassio/ingress/file_api_v2',
  headers: {
    'Authorization': 'Bearer K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA',
    'Content-Type': 'application/json'
  }
});

// Read configuration.yaml
const config = await fileAPI.post('/api/file/read', {
  path: 'configuration.yaml'
});
console.log(config.data.content);
```

### With HA shell_command

```yaml
# configuration.yaml
shell_command:
  backup_config: >
    curl -X POST "http://localhost:8100/api/file/read" 
    -H "Authorization: Bearer K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA"
    -H "Content-Type: application/json"
    -d '{"path": "configuration.yaml"}' > /config/backups/config_$(date +%Y%m%d).yaml
```
