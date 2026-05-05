# Posts Réseaux Sociaux - File API v2

Contenu prêt à copier/coller pour promouvoir votre add-on.

---

## 🎯 Reddit r/homeassistant

### Post 1 : Annonce Release

**Titre** :
```
[Release] File API v2 - Secure REST API for HA Configuration Management
```

**Corps** :
```markdown
Hey r/homeassistant! 👋

I built an add-on that solves a problem I had: **automating Home Assistant configuration changes** without manual copy-paste.

## What is File API v2?

A secure REST API that lets you read/write HA config files programmatically. Perfect for:
- 🤖 Claude Code automation
- 🔄 CI/CD pipelines
- 📦 Automated backups
- 🔗 External tool integrations

## Key Features

✅ **3 Authentication Modes**
   - HA tokens (native, revocable)
   - API secret (automation-friendly)
   - Both (flexible)

✅ **Security First**
   - Path traversal protection
   - File extension whitelist
   - Size limits (1-100 MB)
   - Confined to /config only

✅ **Complete Documentation**
   - Bilingual (FR/EN)
   - 5-minute quickstart
   - Authentication guide

## Installation

```yaml
# Add repository in HA
https://github.com/p3x2007-ops/ha-file-api
```

Then install "File API v2" from the add-on store.

Full guide: [QUICKSTART.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/QUICKSTART.en.md)

## Example Usage

```bash
# Read configuration.yaml
curl -X POST "https://YOUR_INSTANCE/api/hassio/ingress/file_api_v2/api/file/read" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"path": "configuration.yaml"}'
```

## Why I built this

I use Claude Code daily and wanted it to help maintain my HA config. Manual copy-paste was tedious and error-prone. This add-on eliminates that friction.

---

⭐ **[GitHub Repository](https://github.com/p3x2007-ops/ha-file-api)**

Feedback and contributions welcome!

---

*Note: This is NOT for web UI file editing - use File Editor for that. This is for programmatic API access.*
```

---

## 🐦 Twitter/X

### Tweet 1 : Annonce

```
🚀 Just launched File API v2 for #HomeAssistant!

Secure REST API for config file management:
✅ 3 auth modes
✅ Path protection
✅ Perfect for @AnthropicAI Claude Code automation

Automate your HA setup without manual copy-paste 🎯

⭐ https://github.com/p3x2007-ops/ha-file-api

#smarthome #homeautomation #opensource #python
```

### Tweet 2 : Use Case

```
💡 Using Claude Code to maintain your #HomeAssistant config?

File API v2 lets Claude directly read/write your HA files via REST API 🤖

No more copy-paste. Just pure automation.

✨ 3 auth modes
🔒 Path protection
📖 Bilingual docs

https://github.com/p3x2007-ops/ha-file-api

#smarthome #AI
```

### Tweet 3 : Security

```
🔒 Security features in File API v2:

✅ Confined to /config directory
✅ Path traversal protection
✅ File extension whitelist
✅ Size limits (configurable)
✅ Bearer token auth
✅ Complete audit logging

Built for #HomeAssistant automation without compromising security.

https://github.com/p3x2007-ops/ha-file-api
```

---

## 💬 Discord #third-party-addons

### Message 1 : Annonce courte

```
🎉 **File API v2** released!

Secure REST API for reading/writing HA config files. Perfect for Claude Code automation.

Features:
• 3 authentication modes (HA token, API secret, both)
• Path traversal protection
• File extension whitelist
• Size limits
• Bilingual docs (FR/EN)

⭐ https://github.com/p3x2007-ops/ha-file-api

Install: Add repo → Search "File API v2" → Configure auth → Start

Questions? I'm here to help! 🙋‍♂️
```

### Message 2 : Help Request (après quelques jours)

```
Hey everyone! 👋

I released **File API v2** last week (REST API for HA config management).

If anyone has tested it, I'd love your feedback! Particularly:
• Was installation clear?
• Any security concerns?
• Feature requests?

⭐ https://github.com/p3x2007-ops/ha-file-api

Early feedback is super valuable. Thanks! 🙏
```

---

## 📱 LinkedIn (professionnel)

### Post 1 : Annonce professionnelle

```
🚀 Open-Source Project Release: File API v2 for Home Assistant

I'm excited to share a project I've been working on to streamline home automation workflows.

**The Challenge:**
Maintaining Home Assistant configurations often requires manual file editing. For AI-assisted development (Claude Code) or CI/CD pipelines, this creates friction.

**The Solution:**
File API v2 - A secure REST API that provides programmatic access to Home Assistant configuration files.

**Key Features:**
• Multiple authentication modes (Home Assistant tokens, API secrets, or both)
• Security-first design (path traversal protection, file whitelisting, size limits)
• Comprehensive bilingual documentation (French/English)
• MIT licensed

**Use Cases:**
- AI-assisted configuration management
- Automated CI/CD deployments
- Programmatic backups
- External tool integrations

**Tech Stack:**
Python, Flask, Docker, Home Assistant Add-on SDK

This project demonstrates secure API design, container security best practices, and comprehensive documentation standards.

⭐ GitHub: https://github.com/p3x2007-ops/ha-file-api

Open to feedback and contributions from the community!

#opensource #homeautomation #python #docker #api #security #smarthome
```

---

## 📰 Home Assistant Community Forum

### Post : Annonce détaillée

**Titre** :
```
[Add-on] File API v2 - Secure REST API for Configuration Management (v2.0.0)
```

**Catégorie** : Third Party Add-ons

**Tags** : `addon`, `api`, `automation`, `claude-code`, `rest-api`

**Corps** :
```markdown
# File API v2 - Secure REST API for Home Assistant Configuration Management

## 🎯 Overview

File API v2 is a Home Assistant add-on that provides a secure REST API for reading and writing configuration files programmatically.

**Repository:** https://github.com/p3x2007-ops/ha-file-api

## 🚀 Motivation

I built this add-on to solve a specific problem: I use Claude Code (Anthropic's AI coding assistant) to help maintain my Home Assistant configuration, but it couldn't directly access my config files. This meant manual copy-paste for every change.

File API v2 eliminates that friction by providing a secure REST API that Claude Code (or any tool) can use to read and modify HA configs automatically.

## ✨ Key Features

### 3 Authentication Modes
- **`home_assistant`** - Uses native HA tokens (Long-Lived Access Tokens). Recommended for production.
- **`api_secret`** - Custom API secret for simpler automation. Great for CI/CD.
- **`both`** - Accepts either HA token or API secret for maximum flexibility.

### Security Features
- ✅ **Path traversal protection** - Confined to `/config` directory only
- ✅ **File extension whitelist** - Configurable allowed extensions
- ✅ **Size limits** - Configurable max file size (1-100 MB)
- ✅ **Bearer token authentication** - Industry-standard auth
- ✅ **Complete audit logging** - Track all file operations

### Documentation
- ✅ **Bilingual** - Complete docs in French and English
- ✅ **5-minute quickstart** - Get running fast
- ✅ **Authentication guide** - Choose the right mode
- ✅ **Security guide** - Best practices

## 📦 Installation

1. **Add the repository** in Home Assistant:
   - Settings → Add-ons → Add-on Store
   - Menu ⋮ (top right) → Repositories
   - Add: `https://github.com/p3x2007-ops/ha-file-api`
   - Close

2. **Install the add-on**:
   - Refresh the page (F5)
   - Search for "File API v2"
   - Click → Install

3. **Configure authentication**:
   ```yaml
   auth_mode: api_secret  # or home_assistant or both
   api_secret: "your_strong_secret_here"
   ```

4. **Start the add-on**

Full installation guide: [QUICKSTART.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/QUICKSTART.en.md)

## 📡 API Endpoints

- `POST /api/file/read` - Read a file
- `POST /api/file/write` - Write a file
- `POST /api/file/delete` - Delete a file
- `POST /api/file/list` - List directory contents
- `POST /api/file/exists` - Check if file exists
- `GET /health` - Health check

## 💡 Example Usage

```bash
# Read configuration.yaml
curl -X POST \
  "https://YOUR_INSTANCE.ui.nabu.casa/api/hassio/ingress/file_api_v2/api/file/read" \
  -H "Authorization: Bearer YOUR_TOKEN_OR_SECRET" \
  -H "Content-Type: application/json" \
  -d '{"path": "configuration.yaml"}'

# Write a new automation
curl -X POST \
  "https://YOUR_INSTANCE.ui.nabu.casa/api/hassio/ingress/file_api_v2/api/file/write" \
  -H "Authorization: Bearer YOUR_TOKEN_OR_SECRET" \
  -H "Content-Type: application/json" \
  -d '{"path": "automations/new_automation.yaml", "content": "..."}'
```

## 🎯 Use Cases

- **Claude Code automation** - Let AI help maintain your config
- **CI/CD pipelines** - Automated config deployment
- **Backup scripts** - Programmatic config backups
- **Multi-HA sync** - Sync configs between instances
- **External tools** - Any tool needing config file access

## 🔒 Security Considerations

1. **Choose the right auth mode:**
   - Production: `home_assistant` (revocable tokens)
   - Automation: `api_secret` (with strong secret)
   - Development: `both` (flexible testing)

2. **Generate a strong secret:**
   ```bash
   openssl rand -base64 32 | tr -d "=+/" | cut -c1-32
   ```

3. **Network security:**
   - Don't expose directly to Internet
   - Use Home Assistant Cloud (Nabu Casa) or VPN
   - Enable HA firewall

4. **File restrictions:**
   - Limit allowed extensions to what you need
   - Set `max_file_size_mb` appropriately
   - Monitor logs for suspicious activity

Full security guide: [SECURITY.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/SECURITY.md)

## 📖 Documentation

- [README.md](https://github.com/p3x2007-ops/ha-file-api) - Main documentation (bilingual)
- [QUICKSTART.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/QUICKSTART.en.md) - 5-minute setup
- [CONFIGURATION.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/CONFIGURATION.en.md) - Authentication modes explained
- [SECURITY.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/SECURITY.md) - Security best practices
- [CONTRIBUTING.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/CONTRIBUTING.md) - How to contribute

## 🐛 Known Limitations

- Only works via Ingress (not direct port access)
- Single file operations (no batch yet)
- No file versioning/snapshots (planned for v2.1)

## 🗺️ Roadmap

Planned for v2.1.0:
- [ ] Recursive directory operations
- [ ] File search by pattern
- [ ] Compression support (gzip)
- [ ] Rate limiting
- [ ] IP whitelist option

See [CHANGELOG.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/CHANGELOG.md) for full roadmap.

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/CONTRIBUTING.md)

## 📄 License

MIT License - See [LICENSE](https://github.com/p3x2007-ops/ha-file-api/blob/main/LICENSE)

## 💬 Support

- **GitHub Issues**: https://github.com/p3x2007-ops/ha-file-api/issues
- **GitHub Discussions**: https://github.com/p3x2007-ops/ha-file-api/discussions
- **This forum thread**: Ask questions here!

---

⭐ **Star the repository** if you find it useful!

I'm happy to answer questions and take feedback. Let me know what you think!
```

---

## 📝 Dev.to / Medium Article (optionnel)

**Titre** :
```
Automate Your Home Assistant Configuration with Claude Code and File API v2
```

**Tags** : `homeassistant`, `automation`, `python`, `api`, `claudecode`

**Outline** :

1. **Introduction**
   - The problem: Manual config editing is tedious
   - The solution: REST API for programmatic access

2. **What is File API v2?**
   - Overview
   - Key features

3. **Installation Guide**
   - Step-by-step with screenshots

4. **Authentication Modes Explained**
   - When to use each mode
   - Security considerations

5. **Claude Code Integration Example**
   - Real example of AI-assisted config management
   - Commands and workflow

6. **Other Use Cases**
   - CI/CD
   - Backups
   - Multi-instance sync

7. **Security Best Practices**
   - Strong secrets
   - Network isolation
   - Monitoring

8. **Conclusion**
   - Benefits
   - Call to action (GitHub star, contribute)

---

## 🎬 YouTube Video Script (optionnel)

**Titre** : "Automate Home Assistant Config Management with Claude Code | File API v2 Tutorial"

**Duration** : 10-15 minutes

**Script** :

1. **Intro (0:00-0:30)**
   - Hook: "Tired of manually editing HA config files?"
   - What we'll cover today

2. **Problem Statement (0:30-2:00)**
   - Manual editing is tedious
   - AI can't access files directly
   - Need for automation

3. **Solution Overview (2:00-3:00)**
   - Introduce File API v2
   - Key features quick overview

4. **Installation Demo (3:00-6:00)**
   - Show HA UI
   - Add repository
   - Install add-on
   - Configure authentication
   - Start add-on

5. **API Demo (6:00-9:00)**
   - Show curl examples
   - Read a file
   - Write a file
   - List directory

6. **Claude Code Integration (9:00-12:00)**
   - Show Claude Code interface
   - Give it File API access
   - Watch it modify HA config
   - Show the changes in HA

7. **Security Tips (12:00-13:00)**
   - Strong secrets
   - Auth mode selection
   - Network isolation

8. **Outro (13:00-15:00)**
   - Recap benefits
   - GitHub link
   - Call to action (like, subscribe, star repo)

---

**Tous ces contenus sont prêts à utiliser ! 🚀**

Choisissez les plateformes qui vous intéressent et adaptez selon votre style.
