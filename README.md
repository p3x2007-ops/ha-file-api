# File API v2 - Home Assistant Add-on

API REST sécurisée permettant à Claude Code et autres outils d'automatiser la gestion des fichiers dans Home Assistant.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Add--on-blue.svg)](https://www.home-assistant.io/)

**🚀 [Démarrage rapide (5 min) →](#-installation-rapide)**

## 🎯 Fonctionnalités

- ✅ Lecture de fichiers (`/api/file/read`)
- ✅ Écriture de fichiers (`/api/file/write`)
- ✅ Suppression de fichiers (`/api/file/delete`)
- ✅ Listage de répertoires (`/api/file/list`)
- ✅ Vérification d'existence (`/api/file/exists`)
- 🔒 Protection contre les path traversal
- 📏 Limite de taille de fichiers configurable
- 🎨 Extensions de fichiers autorisées configurables
- 📝 Logging complet

## 🚀 Installation rapide

### Via GitHub (Recommandé)

1. **Dans Home Assistant** :
   - Paramètres → Modules complémentaires → Boutique des modules complémentaires
   - Menu ⋮ (en haut à droite) → Repositories
   - Ajouter : `https://github.com/p3x2007-ops/ha-file-api`
   - Fermer

2. **Installer** :
   - Rafraîchir la page (F5)
   - Chercher "File API v2"
   - Cliquer → Installer
   - Attendre la fin du build (1-2 min)

3. **Configurer** :
   - Onglet "Configuration"
   - Définir votre mode d'authentification (voir ci-dessous)
   - Sauvegarder

4. **Démarrer** :
   - Activer "Démarrer au boot" et "Watchdog"
   - Cliquer sur "DÉMARRER"

### Via installation locale

1. Créer `/config/addons/file_api_v2/`
2. Télécharger les fichiers du dossier `file_api_v2/` depuis ce repository
3. Uploader dans le dossier créé
4. Ajouter repository local : `/config/addons`
5. Installer depuis "Local add-ons"

## 🔐 Authentification

File API v2 offre **3 modes d'authentification** :

| Mode | Description | Utilisation |
|------|-------------|-------------|
| `home_assistant` | Token HA natif (défaut) | Maximum sécurité |
| `api_secret` | Secret personnalisé | Automatisation simple |
| `both` | Les deux acceptés | Maximum flexibilité |

**Configuration rapide (recommandé pour Claude) :**

1. Après installation, ouvrir **Configuration de l'addon**
2. Définir :
   ```yaml
   auth_mode: api_secret
   api_secret: "VOTRE_SECRET_ICI"  # Générez un secret fort !
   ```
3. Sauvegarder et redémarrer

**Générer un secret fort :**
```bash
openssl rand -base64 32 | tr -d "=+/" | cut -c1-32
```

## ⚙️ Autres paramètres

```yaml
log_level: info              # debug, info, warning, error
max_file_size_mb: 10         # Taille max des fichiers (1-100 MB)
allowed_extensions:          # Extensions autorisées
  - .yaml
  - .yml
  - .json
  - .js
  - .py
  - .md
  - .txt
  - .sh
```

## 📡 API Endpoints

### Health Check
```bash
GET /health
```

**Réponse:**
```json
{"status": "healthy", "version": "1.0.0"}
```

---

### Lire un fichier
```bash
POST /api/file/read
Content-Type: application/json

{
  "path": "/www/dolce-gusto-card.js"
}
```

**Réponse:**
```json
{
  "success": true,
  "path": "/www/dolce-gusto-card.js",
  "content": "// file content here...",
  "size": 31744
}
```

---

### Écrire un fichier
```bash
POST /api/file/write
Content-Type: application/json

{
  "path": "/www/test.js",
  "content": "console.log('hello');"
}
```

**Réponse:**
```json
{
  "success": true,
  "path": "/www/test.js",
  "size": 23
}
```

---

### Supprimer un fichier
```bash
POST /api/file/delete
Content-Type: application/json

{
  "path": "/www/test.js"
}
```

**Réponse:**
```json
{
  "success": true,
  "path": "/www/test.js"
}
```

---

### Lister un répertoire
```bash
POST /api/file/list
Content-Type: application/json

{
  "path": "/www"
}
```

**Réponse:**
```json
{
  "success": true,
  "path": "/www",
  "files": [
    {
      "name": "dolce-gusto-card.js",
      "is_dir": false,
      "size": 31744,
      "modified": 1746389760
    },
    {
      "name": "community",
      "is_dir": true,
      "size": 0,
      "modified": 1746300000
    }
  ]
}
```

---

### Vérifier existence
```bash
POST /api/file/exists
Content-Type: application/json

{
  "path": "/www/test.js"
}
```

**Réponse:**
```json
{
  "success": true,
  "path": "/www/test.js",
  "exists": true,
  "is_file": true,
  "is_dir": false
}
```

## 🔒 Sécurité

- ✅ Tous les chemins sont validés contre le path traversal
- ✅ Limité au répertoire `/config` uniquement
- ✅ Extensions de fichiers contrôlées
- ✅ Taille de fichiers limitée
- ✅ Pas d'exécution de code
- ✅ Logging de toutes les opérations

## 🧪 Test depuis Claude Code

```bash
# Définir les variables (remplacez par vos valeurs)
HA_URL="https://YOUR_INSTANCE.ui.nabu.casa"
HA_TOKEN="YOUR_LONG_LIVED_ACCESS_TOKEN"
API_URL="${HA_URL}/api/hassio/ingress/file_api_v2"

# Lire configuration.yaml
curl -X POST "${API_URL}/api/file/read" \
  -H "Authorization: Bearer $HA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"path": "configuration.yaml"}'

# Écrire un fichier test
curl -X POST "${API_URL}/api/file/write" \
  -H "Authorization: Bearer $HA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"path": "www/test.txt", "content": "Hello from Claude!"}'

# Lister /www
curl -X POST "${API_URL}/api/file/list" \
  -H "Authorization: Bearer $HA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"path": "www"}'
```

## 📊 Logs & Troubleshooting

**Logs :** Interface add-on → Onglet "Journal"

**Erreurs courantes :**

| Erreur | Solution |
|--------|----------|
| HTTP 401 "Invalid token" | Vérifier auth_mode et utiliser le bon token |
| HTTP 403 "Path traversal" | Utiliser chemin relatif : `www/test.js` |
| HTTP 413 "File too large" | Augmenter `max_file_size_mb` |
| HTTP 403 "Extension not allowed" | Ajouter extension dans `allowed_extensions` |

## 🔄 Mise à jour

Dans Home Assistant : Paramètres → Modules complémentaires → File API v2 → Mise à jour disponible → Mettre à jour

## 📄 Licence

MIT

## 👤 Auteur

Créé pour automatiser les interactions Claude Code avec Home Assistant.
