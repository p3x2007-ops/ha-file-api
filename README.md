# File API Add-on pour Home Assistant

API REST sécurisée permettant à Claude Code de lire et modifier les fichiers de configuration Home Assistant.

**🚀 [Démarrage rapide (5 min) →](QUICKSTART.md)**

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

## 🚀 Installation

### Méthode 1 : Repository local (Recommandé)

1. **Créer le dossier de l'add-on dans Home Assistant**
   ```bash
   # Via File Editor, créer la structure:
   /config/addons/file_api/
   ```

2. **Uploader les fichiers de l'add-on**
   - Via File Editor, uploader dans `/config/addons/file_api/` :
     - `config.yaml`
     - `Dockerfile`
     - `build.yaml`
     - `server.py`
     - `run.sh`
     - `README.md`

3. **Ajouter le repository local**
   - Paramètres → Modules complémentaires → Boutique des modules complémentaires
   - Menu 3 points (en haut à droite) → Repositories
   - Ajouter : `/config/addons`

4. **Installer l'add-on**
   - Rafraîchir la page
   - Chercher "File API" dans la liste
   - Installer et démarrer

### Méthode 2 : GitHub (Alternative)

Si vous créez un repository GitHub :

1. Créer un repo avec la structure ci-dessus
2. Dans HA : Paramètres → Modules complémentaires → Boutique
3. Ajouter repository : `https://github.com/p3x2007-ops/ha-file-api`

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

**📖 Guide complet :** Voir [CONFIGURATION.md](CONFIGURATION.md)

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

## 📊 Logs

Les logs sont accessibles via :
- Interface de l'add-on → Onglet "Journal"
- Ou via : Paramètres → Système → Journaux → file_api

## ❓ Troubleshooting

**L'add-on ne démarre pas**
- Vérifier les logs : Onglet "Journal" de l'add-on
- Vérifier la configuration YAML
- Redémarrer l'add-on

**Erreur 403 "Path traversal detected"**
- Le chemin contient `..` ou des tentatives de sortir de `/config`
- Utiliser uniquement des chemins relatifs : `www/test.js` pas `/config/www/test.js`

**Erreur 413 "File too large"**
- Augmenter `max_file_size_mb` dans la configuration
- Maximum : 100 MB

**Erreur 403 "File extension not allowed"**
- Ajouter l'extension dans `allowed_extensions`
- Exemples : `.css`, `.xml`, `.conf`

## 🔄 Mise à jour

1. Mettre à jour les fichiers dans `/config/addons/file_api/`
2. Reconstruire l'add-on : Menu → "Rebuild"
3. Redémarrer

## 📝 Changelog

### v1.0.0 (2026-05-04)
- 🎉 Version initiale
- ✅ Endpoints read/write/delete/list/exists
- 🔒 Sécurité path traversal
- 📏 Limite de taille configurable
- 🎨 Extensions configurables

## 📄 Licence

MIT

## 👤 Auteur

Créé pour automatiser les interactions Claude Code avec Home Assistant.
