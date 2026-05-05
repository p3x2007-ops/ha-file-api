# File API v2 - Home Assistant Add-on

🇫🇷 **Français** | 🇬🇧 [English](#english-version)

---

API REST sécurisée permettant à Claude Code et autres outils de lire et modifier les fichiers de configuration Home Assistant.

Secure REST API allowing Claude Code and other tools to read and modify Home Assistant configuration files.

## 🎯 Fonctionnalités

- ✅ Lecture de fichiers (`/api/file/read`)
- ✅ Écriture de fichiers (`/api/file/write`)
- ✅ Suppression de fichiers (`/api/file/delete`)
- ✅ Listage de répertoires (`/api/file/list`)
- ✅ Vérification d'existence (`/api/file/exists`)
- 🔒 3 modes d'authentification (HA token, API secret, both)
- 🔒 Protection contre les path traversal
- 📏 Limite de taille de fichiers configurable
- 🎨 Extensions de fichiers autorisées configurables

## 🚀 Installation

### Via ce repository GitHub

1. **Ajouter le repository** dans Home Assistant :
   - Paramètres → Modules complémentaires → Boutique des modules complémentaires
   - Menu ⋮ (en haut à droite) → Repositories
   - Ajouter : `https://github.com/p3x2007-ops/ha-file-api`
   - Fermer

2. **Installer l'add-on** :
   - Rafraîchir la page (F5)
   - Chercher "File API v2"
   - Cliquer → Installer
   - Attendre la fin du build (1-2 min)

3. **Configurer l'authentification** :
   - Onglet "Configuration"
   - Choisir le mode d'authentification :
     ```yaml
     auth_mode: api_secret  # ou home_assistant ou both
     api_secret: "votre_secret_ici"  # Si mode api_secret
     ```
   - Sauvegarder

4. **Démarrer** :
   - Activer "Démarrer au boot" et "Watchdog"
   - Cliquer sur "DÉMARRER"

### Via installation locale

Si vous préférez l'installation locale :

1. Créer `/config/addons/file_api_v2/`
2. Télécharger et uploader les fichiers de ce dossier
3. Ajouter repository local : `/config/addons`
4. Installer depuis "Local add-ons"

## 🔐 Authentification

File API v2 offre **3 modes d'authentification** :

### Mode 1 : Home Assistant Token (défaut)
```yaml
auth_mode: home_assistant
api_secret: ""
```
Utilise les tokens Home Assistant natifs (Long-Lived Access Token).

### Mode 2 : API Secret (recommandé pour Claude Code)
```yaml
auth_mode: api_secret
api_secret: "mon_secret_securise_123"
```
Secret personnalisé, plus simple pour l'automatisation.

### Mode 3 : Both (les deux)
```yaml
auth_mode: both
api_secret: "mon_secret_123"
```
Accepte soit le token HA, soit votre API secret.

**Générer un secret fort :**
```bash
openssl rand -base64 32 | tr -d "=+/" | cut -c1-32
```

## 📡 Utilisation

### Health Check
```bash
curl https://YOUR_INSTANCE.ui.nabu.casa/api/hassio/ingress/file_api_v2/health
```

### Lire un fichier
```bash
curl -X POST \
  "https://YOUR_INSTANCE.ui.nabu.casa/api/hassio/ingress/file_api_v2/api/file/read" \
  -H "Authorization: Bearer YOUR_TOKEN_OR_SECRET" \
  -H "Content-Type: application/json" \
  -d '{"path": "configuration.yaml"}'
```

### Écrire un fichier
```bash
curl -X POST \
  "https://YOUR_INSTANCE.ui.nabu.casa/api/hassio/ingress/file_api_v2/api/file/write" \
  -H "Authorization: Bearer YOUR_TOKEN_OR_SECRET" \
  -H "Content-Type: application/json" \
  -d '{"path": "www/test.txt", "content": "Hello!"}'
```

## 🔒 Sécurité

- ✅ Accès limité au répertoire `/config` uniquement
- ✅ Protection contre le path traversal
- ✅ Extensions de fichiers contrôlées
- ✅ Taille de fichiers limitée (10 MB par défaut, configurable jusqu'à 100 MB)
- ✅ Authentification Bearer obligatoire
- ✅ Logging complet de toutes les opérations

## ⚙️ Configuration

```yaml
# Mode d'authentification
auth_mode: api_secret  # home_assistant | api_secret | both

# Secret API (si mode api_secret ou both)
api_secret: "votre_secret_fort"

# Niveau de logs
log_level: info  # debug | info | warning | error

# Extensions autorisées
allowed_extensions:
  - .yaml
  - .yml
  - .json
  - .js
  - .py
  - .md
  - .txt
  - .sh

# Taille max fichiers (MB)
max_file_size_mb: 10  # 1-100
```

## 📖 Documentation complète

Pour plus de détails, consultez la documentation dans le repository principal :
- [QUICKSTART.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/QUICKSTART.md) - Démarrage en 5 minutes ([🇬🇧 English](https://github.com/p3x2007-ops/ha-file-api/blob/main/QUICKSTART.en.md))
- [CONFIGURATION.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/CONFIGURATION.md) - Guide complet d'authentification ([🇬🇧 English](https://github.com/p3x2007-ops/ha-file-api/blob/main/CONFIGURATION.en.md))
- [README.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/README.md) - Documentation principale

## 🐛 Troubleshooting

### Erreur 401 "Invalid or expired token"
- Vérifier le mode d'auth : `curl .../health`
- Si `api_secret` : utiliser votre secret
- Si `home_assistant` : utiliser token HA

### Erreur 403 "Path traversal detected"
- Utiliser chemin relatif : `www/file.js` (pas `/config/www/file.js`)

### Erreur 413 "File too large"
- Augmenter `max_file_size_mb` dans la configuration

## 📝 Changelog

### v2.0.0 (2026-05-04)
- 🎉 Modes d'authentification configurables (HA token, API secret, both)
- ✨ Configuration via UI addon
- 📖 Documentation complète en français
- 🔒 Sécurité renforcée

## 📄 Licence

MIT

## 👤 Auteur

Créé pour automatiser les interactions Claude Code avec Home Assistant.

---

# English Version

Secure REST API for managing Home Assistant configuration files via Claude Code and automation tools.

## 🎯 Features

- ✅ Read files (`/api/file/read`)
- ✅ Write files (`/api/file/write`)
- ✅ Delete files (`/api/file/delete`)
- ✅ List directories (`/api/file/list`)
- ✅ Check file existence (`/api/file/exists`)
- 🔒 3 authentication modes (HA token, API secret, both)
- 🔒 Path traversal protection
- 📏 Configurable file size limit
- 🎨 Configurable allowed file extensions

## 🚀 Installation

### Via this GitHub repository

1. **Add the repository** in Home Assistant:
   - Settings → Add-ons → Add-on Store
   - Menu ⋮ (top right) → Repositories
   - Add: `https://github.com/p3x2007-ops/ha-file-api`
   - Close

2. **Install the add-on**:
   - Refresh the page (F5)
   - Search for "File API v2"
   - Click → Install
   - Wait for build to complete (1-2 min)

3. **Configure authentication**:
   - "Configuration" tab
   - Choose authentication mode:
     ```yaml
     auth_mode: api_secret  # or home_assistant or both
     api_secret: "your_secret_here"  # If api_secret mode
     ```
   - Save

4. **Start**:
   - Enable "Start on boot" and "Watchdog"
   - Click "START"

### Via local installation

If you prefer local installation:

1. Create `/config/addons/file_api_v2/`
2. Download and upload files from this folder
3. Add local repository: `/config/addons`
4. Install from "Local add-ons"

## 🔐 Authentication

File API v2 offers **3 authentication modes**:

### Mode 1: Home Assistant Token (default)
```yaml
auth_mode: home_assistant
api_secret: ""
```
Uses native Home Assistant tokens (Long-Lived Access Token).

### Mode 2: API Secret (recommended for Claude Code)
```yaml
auth_mode: api_secret
api_secret: "my_secure_secret_123"
```
Custom secret, simpler for automation.

### Mode 3: Both
```yaml
auth_mode: both
api_secret: "my_secret_123"
```
Accepts either HA token or your API secret.

**Generate a strong secret:**
```bash
openssl rand -base64 32 | tr -d "=+/" | cut -c1-32
```

## 📡 Usage

### Health Check
```bash
curl https://YOUR_INSTANCE.ui.nabu.casa/api/hassio/ingress/file_api_v2/health
```

### Read a file
```bash
curl -X POST \
  "https://YOUR_INSTANCE.ui.nabu.casa/api/hassio/ingress/file_api_v2/api/file/read" \
  -H "Authorization: Bearer YOUR_TOKEN_OR_SECRET" \
  -H "Content-Type: application/json" \
  -d '{"path": "configuration.yaml"}'
```

### Write a file
```bash
curl -X POST \
  "https://YOUR_INSTANCE.ui.nabu.casa/api/hassio/ingress/file_api_v2/api/file/write" \
  -H "Authorization: Bearer YOUR_TOKEN_OR_SECRET" \
  -H "Content-Type: application/json" \
  -d '{"path": "www/test.txt", "content": "Hello!"}'
```

## 🔒 Security

- ✅ Access limited to `/config` directory only
- ✅ Path traversal protection
- ✅ Controlled file extensions
- ✅ File size limit (10 MB default, configurable up to 100 MB)
- ✅ Mandatory Bearer authentication
- ✅ Complete logging of all operations

## ⚙️ Configuration

```yaml
# Authentication mode
auth_mode: api_secret  # home_assistant | api_secret | both

# API secret (if api_secret or both mode)
api_secret: "your_strong_secret"

# Log level
log_level: info  # debug | info | warning | error

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
max_file_size_mb: 10  # 1-100
```

## 📖 Full Documentation

For more details, check the documentation in the main repository:
- [QUICKSTART.en.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/QUICKSTART.en.md) - 5-minute quickstart
- [CONFIGURATION.en.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/CONFIGURATION.en.md) - Complete authentication guide
- [README.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/README.md) - Main documentation (bilingual)

## 🐛 Troubleshooting

### Error 401 "Invalid or expired token"
- Check auth mode: `curl .../health`
- If `api_secret`: use your secret
- If `home_assistant`: use HA token

### Error 403 "Path traversal detected"
- Use relative path: `www/file.js` (not `/config/www/file.js`)

### Error 413 "File too large"
- Increase `max_file_size_mb` in configuration

## 📝 Changelog

### v2.0.0 (2026-05-04)
- 🎉 Configurable authentication modes (HA token, API secret, both)
- ✨ Configuration via add-on UI
- 📖 Complete bilingual documentation (French/English)
- 🔒 Enhanced security

## 📄 License

MIT

## 👤 Author

Created to automate Claude Code interactions with Home Assistant.
