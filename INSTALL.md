# Installation rapide File API Add-on

## 📦 Fichiers à uploader

Tous les fichiers sont disponibles dans ce repository GitHub.

## 🚀 Installation (10 minutes)

### Étape 1 : Créer la structure dans Home Assistant (2 min)

1. Ouvrir **File Editor** dans Home Assistant
2. Naviguer vers la racine (`/config`)
3. Créer un dossier **`addons`** (si n'existe pas)
4. Dans `addons`, créer un dossier **`file_api`**

**Résultat attendu :**
```
/config/
├── addons/
│   └── file_api/    ← Nouveau dossier vide
```

### Étape 2 : Uploader les fichiers (5 min)

**Via File Editor :**

1. Naviguer vers `/config/addons/file_api_v2/`
2. Télécharger ou cloner ce repository, puis uploader les fichiers essentiels :
   - ✅ `config.yaml`
   - ✅ `Dockerfile`
   - ✅ `build.yaml`
   - ✅ `server.py`
   - ✅ `run.sh`
   - ✅ `README.md` (optionnel)

**Résultat attendu :**
```
/config/addons/file_api_v2/
├── config.yaml      ← ~1.0 KB
├── Dockerfile       ← ~0.4 KB
├── build.yaml       ← ~0.3 KB
├── server.py        ← ~11 KB
├── run.sh           ← ~0.5 KB
└── README.md        ← ~6.5 KB (optionnel)
```

### Étape 3 : Ajouter le repository local (1 min)

1. **Paramètres** → **Modules complémentaires**
2. **Boutique des modules complémentaires** (en bas à droite)
3. Cliquer sur le **menu 3 points** (⋮) en haut à droite
4. **Repositories**
5. Ajouter : `/config/addons`
6. Cliquer **Ajouter**
7. **Fermer** la fenêtre

### Étape 4 : Installer l'add-on (2 min)

1. **Rafraîchir la page** (Cmd+R ou F5)
2. Descendre dans la section **"Local add-ons"**
3. Vous devriez voir : **"File API"**
4. Cliquer dessus
5. Cliquer **Installer** (attendre 1-2 minutes pour le build)
6. Une fois installé, activer :
   - ✅ **Démarrer au boot**
   - ✅ **Watchdog**
7. Cliquer **Démarrer**

### Étape 5 : Vérifier (30 sec)

**Onglet "Journal" de l'add-on :**
```
[INFO] Starting File API Server v1.0.0
[INFO] Base path: /config
[INFO] Max file size: 10 MB
[INFO] Allowed extensions: {'.yaml', '.yml', '.json', '.js', '.py', '.md', '.txt', '.sh'}
```

**Onglet "Info" :**
- État : ✅ Started
- Port : 8100/tcp

## ✅ Test de l'installation

### Test 1 : Health check

```bash
# Remplacez par votre URL Nabu Casa ou URL locale
HA_URL="https://YOUR_INSTANCE.ui.nabu.casa"

# Générez un Long-Lived Access Token dans HA : Profil → Tokens d'accès de longue durée
HA_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.YOUR_TOKEN_HERE"

curl -s "${HA_URL}/api/hassio/ingress/file_api_v2/health" \
  -H "Authorization: Bearer $HA_TOKEN" | python3 -m json.tool
```

**Résultat attendu :**
```json
{
    "status": "healthy",
    "version": "1.0.0"
}
```

### Test 2 : Lire configuration.yaml

```bash
curl -s -X POST "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/read" \
  -H "Authorization: Bearer $HA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"path": "configuration.yaml"}' | python3 -m json.tool | head -20
```

**Résultat attendu :** Contenu de votre `configuration.yaml`

### Test 3 : Écrire un fichier test

```bash
curl -s -X POST "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/write" \
  -H "Authorization: Bearer $HA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"path": "www/test_api.txt", "content": "Hello from File API!"}' | python3 -m json.tool
```

**Résultat attendu :**
```json
{
    "success": true,
    "path": "www/test_api.txt",
    "size": 21
}
```

### Test 4 : Vérifier que le fichier existe

Via File Editor : `/config/www/test_api.txt` doit contenir : `Hello from File API!`

## 🎉 Installation terminée !

Claude peut maintenant :
- ✅ Lire tous les fichiers dans `/config/`
- ✅ Écrire des fichiers (cards, configs, scripts)
- ✅ Supprimer des fichiers
- ✅ Lister des répertoires
- ✅ Automatiser 100% des modifications HA

## 🔄 Utilisation avec Claude

Claude utilisera automatiquement l'API pour :
- Mettre à jour les cards custom
- Modifier configuration.yaml
- Créer/modifier des automations
- Uploader des scripts
- Et bien plus !

**Plus besoin d'upload manuel !** 🚀

## ❓ Problèmes ?

### L'add-on ne démarre pas
- Vérifier logs : Onglet "Journal"
- Vérifier que tous les fichiers sont uploadés
- Rebuilder : Menu → "Rebuild"

### Erreur "Repository not found"
- Vérifier le chemin : `/config/addons` (pas `addons/` seul)
- Rafraîchir la page après ajout du repository

### Build échoue
- Vérifier `build.yaml` et `Dockerfile` bien uploadés
- Vérifier syntaxe YAML (pas de tabs, espaces uniquement)
- Consulter logs de build

## 📝 Configuration avancée

**Configuration de l'add-on** (onglet Configuration) :

```yaml
log_level: info        # debug pour plus de détails
max_file_size_mb: 10   # Augmenter si besoin (max 100)
allowed_extensions:
  - .yaml
  - .yml
  - .json
  - .js
  - .py
  - .md
  - .txt
  - .sh
  - .css              # Ajouter si besoin
  - .xml              # Ajouter si besoin
```

## 🔐 Sécurité

- ✅ Accès uniquement via token HA
- ✅ Limité à `/config` uniquement
- ✅ Protection path traversal
- ✅ Extensions contrôlées
- ✅ Taille max fichiers
- ✅ Logging complet

**Note :** L'add-on ne peut PAS accéder à :
- `/`
- `/root`
- `/etc`
- Autres répertoires système

Seulement `/config` (votre configuration HA).
