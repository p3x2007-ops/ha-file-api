# File API v2 - Home Assistant Add-on

API REST sécurisée permettant à Claude Code et autres outils de lire et modifier les fichiers de configuration Home Assistant.

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
- [QUICKSTART.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/QUICKSTART.md) - Démarrage en 5 minutes
- [CONFIGURATION.md](https://github.com/p3x2007-ops/ha-file-api/blob/main/CONFIGURATION.md) - Guide complet d'authentification
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
