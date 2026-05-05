# 🚀 Quick Start - File API v2

**5-minute** guide to install and configure File API v2.

## Step 1: Install the add-on (2 min)

### Via File Editor

1. **Create folder** `/config/addons/file_api_v2/`

2. **Upload files** from your computer:
   - `config.yaml`
   - `Dockerfile`
   - `build.yaml`
   - `server.py`
   - `run.sh`

3. **Add local repository**
   - Settings → Add-ons → Add-on Store → ⋮ → Repositories
   - Add: `/config/addons`
   - Refresh the page

4. **Install**
   - Search for "File API v2"
   - Click → Install
   - Wait for completion (1-2 min)

## Step 2: Configure authentication (1 min)

### Option A: API Secret (Recommended for Claude)

1. **Generate a strong secret** (Terminal):
   ```bash
   openssl rand -base64 32 | tr -d "=+/" | cut -c1-32
   ```
   
   Example result: `K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA`

2. **Configure the add-on**:
   - "Configuration" tab
   - Modify:
     ```yaml
     auth_mode: api_secret
     api_secret: "K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA"
     ```
   - **Save**

3. **Start the add-on** → "START" button

### Option B: Home Assistant Token

1. **Create an HA token**:
   - Profile (bottom left) → Long-lived access tokens
   - **Create token** (name: "File API Claude")
   - **Copy the token**

2. **Leave default config**:
   ```yaml
   auth_mode: home_assistant
   api_secret: ""
   ```

3. **Start the add-on**

## Step 3: Test (1 min)

### With API Secret

```bash
HA_URL="https://YOUR_INSTANCE.ui.nabu.casa"
SECRET="K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA"

# Health check
curl -s "${HA_URL}/api/hassio/ingress/file_api_v2/health"

# List /config/www/
curl -s -X POST "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/list" \
  -H "Authorization: Bearer ${SECRET}" \
  -H "Content-Type: application/json" \
  -d '{"path": "www"}'
```

### With HA Token

```bash
HA_URL="https://YOUR_INSTANCE.ui.nabu.casa"
HA_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# List /config/www/
curl -s -X POST "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/list" \
  -H "Authorization: Bearer ${HA_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"path": "www"}'
```

**✅ If you see `"success": true` → The add-on works!**

## Step 4: Use with Claude Code (1 min)

### Save the secret in Claude

1. Open a conversation with Claude Code

2. Provide the secret:
   ```
   My File API secret is: K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA
   
   Home Assistant URL: https://YOUR_INSTANCE.ui.nabu.casa
   ```

3. Claude can now automate modifications:
   ```
   "Update the Dolce Gusto card to change the color"
   ```

Claude will:
1. ✅ Download `dolce-gusto-card.js` via File API
2. ✅ Modify the file locally
3. ✅ Upload automatically via File API
4. ✅ Done - No manual action!

## 📊 Verification

### In add-on logs

**Settings → Add-ons → File API v2 → Log**

You should see:
```
Starting File API Server v2.0.0 (with authentication)
Base path: /config
Max file size: 10 MB
Authentication mode: api_secret
API Secret configured: K7mP9nQ2...
```

### Health check

```bash
curl -s "${HA_URL}/api/hassio/ingress/file_api_v2/health"
```

**Expected result:**
```json
{
  "status": "healthy",
  "version": "2.0.0",
  "auth_mode": "api_secret",
  "api_secret_configured": true
}
```

## ❓ Common Issues

### "Invalid or expired token"

**Cause:** Incorrect token or misconfigured mode.

**Solution:**
1. Check mode in `/health`
2. If `api_secret` → Use your secret
3. If `home_assistant` → Use HA token

### "API Secret NOT configured"

**Cause:** Mode `api_secret` but empty field.

**Solution:**
1. Open add-on configuration
2. Fill `api_secret: "your_secret"`
3. Save and restart

### Add-on won't start

**Cause:** Error in Dockerfile or missing dependencies.

**Solution:**
1. Check logs: Log tab
2. Rebuild: Options → Rebuild
3. If error persists, copy logs and open GitHub issue

## 🎉 You're ready!

File API v2 is now operational. Claude Code can automate 100% of your Home Assistant file modifications.

**Next steps:**
- 📖 Read [CONFIGURATION.md](CONFIGURATION.md) for advanced options
- 🔒 Read [SECURITY_CHECK.md](SECURITY_CHECK.md) for best practices
- 🚀 Test with a real modification via Claude

**Need help?** Open an issue on GitHub.
