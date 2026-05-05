# File API v2 - Secure REST API for Home Assistant Configuration Management

## 🎯 What is it?

File API v2 is a Home Assistant add-on that provides a secure REST API for reading and writing configuration files. It's designed primarily for **Claude Code** automation but works with any REST client.

## ✨ Key Features

- ✅ **Read, Write, Delete** files via REST API
- ✅ **3 authentication modes**: HA token, API secret, or both
- ✅ **Path traversal protection** - confined to `/config` directory
- ✅ **File extension whitelist** - configurable allowed extensions
- ✅ **Size limits** - configurable max file size (1-100 MB)
- ✅ **Complete audit logs** - track all file operations
- ✅ **Bilingual documentation** - French and English

## 🔌 Why I built this

I wanted to use **Claude Code** to help me maintain my Home Assistant configuration without manual copy-paste. This add-on allows Claude (or any automation tool) to directly read and modify HA config files via a secure API.

## 🚀 Installation

1. Add repository: `https://github.com/p3x2007-ops/ha-file-api`
2. Install "File API v2" add-on
3. Configure authentication mode
4. Start the add-on

Full installation guide: [QUICKSTART.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/QUICKSTART.md)

## 🔐 Security

- Restricted to `/config` directory only
- Bearer token authentication required
- File extension validation
- Size limits enforced
- Complete operation logging
- Path traversal protection

**Recommendation**: Use `auth_mode: home_assistant` in production (revocable tokens), or `api_secret` for automation with a strong generated secret.

## 📖 Documentation

- [README.md](https://github.com/p3x2007-ops/ha-file-api) - Main documentation (bilingual)
- [QUICKSTART.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/QUICKSTART.md) - 5-minute setup guide
- [CONFIGURATION.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/CONFIGURATION.md) - Authentication modes explained

## 🎯 Use Cases

- **Claude Code automation**: Let AI help maintain your HA config
- **CI/CD pipelines**: Automated config deployment
- **Backup scripts**: Programmatic config backups
- **Multi-HA sync**: Sync configs between instances
- **External tools**: Any tool needing config file access

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/CONTRIBUTING.md)

## 📝 Example Usage

```bash
# Read configuration.yaml
curl -X POST "https://YOUR_INSTANCE.ui.nabu.casa/api/hassio/ingress/file_api_v2/api/file/read" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"path": "configuration.yaml"}'

# Write a new automation
curl -X POST "https://YOUR_INSTANCE.ui.nabu.casa/api/hassio/ingress/file_api_v2/api/file/write" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"path": "automations/new_automation.yaml", "content": "..."}'
```

## 🔗 Links

- **Repository**: https://github.com/p3x2007-ops/ha-file-api
- **Issues**: https://github.com/p3x2007-ops/ha-file-api/issues
- **Discussions**: https://github.com/p3x2007-ops/ha-file-api/discussions

---

**Star the repo** if you find it useful! ⭐

Feedback and contributions welcome!
