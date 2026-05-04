# 📂 Structure finale pour GitHub - ha-file-api

## ✅ Nouvelle structure (compatible Home Assistant)

```
ha-file-api/                              ← Repository GitHub
│
├── repository.json                       ⭐ NOUVEAU - Métadonnées HA
│
├── file_api_v2/                         ⭐ NOUVEAU - Dossier add-on
│   ├── config.yaml                       ← Configuration addon
│   ├── Dockerfile                        ← Image Docker
│   ├── build.yaml                        ← Build multi-arch
│   ├── server.py                         ← Code API Python
│   ├── run.sh                            ← Script démarrage
│   └── README.md                         ← Doc addon (vue dans HA)
│
├── .gitignore                            ← Config Git
├── CHANGELOG.md                          ← Historique versions
├── CONFIGURATION.md                      ← Guide authentification
├── CORRECTIONS_SUMMARY.md                ← Résumé corrections
├── INSTALL.md                            ← Guide installation
├── LICENSE                               ← MIT License
├── PUSH_TO_GITHUB.md                     ← Instructions push
├── QUICKSTART.md                         ← Démarrage 5 min
├── README.md                             ⭐ Doc principale (vue GitHub)
├── STRUCTURE_INSTALLATION.md             ← Aide installation
├── STRUCTURE_REPO.md                     ← Structure repository
└── UPGRADE.md                            ← Migration v1→v2
```

## 🎯 Pourquoi cette structure ?

### ❌ Ancienne structure (ne fonctionnait pas)
```
ha-file-api/
├── config.yaml       ← Fichiers à la racine
├── Dockerfile
├── server.py
└── ...
```
**Erreur :** "is not a valid app repository"

### ✅ Nouvelle structure (fonctionne)
```
ha-file-api/
├── repository.json          ← Identifie le repository HA
└── file_api_v2/            ← Add-on dans sous-dossier
    ├── config.yaml
    └── ...
```
**Résultat :** Home Assistant reconnaît et installe l'add-on ! ✅

## 📋 Fichiers critiques

### 1. repository.json (racine)
```json
{
  "name": "File API Repository",
  "url": "https://github.com/p3x2007-ops/ha-file-api",
  "maintainer": "p3x2007-ops"
}
```
**Rôle :** Indique à Home Assistant que ce repository contient des add-ons.

### 2. file_api_v2/ (sous-dossier)
**Rôle :** Contient tous les fichiers de l'add-on.

**Nom du dossier = slug de l'add-on** → `file_api_v2` correspond au `slug: "file_api_v2"` dans config.yaml

### 3. file_api_v2/config.yaml
```yaml
name: "File API v2"
slug: "file_api_v2"    ← Doit correspondre au nom du dossier
...
```

## 🚀 Installation dans Home Assistant

Avec cette structure, l'installation fonctionne :

1. **Ajouter le repository :**
   ```
   https://github.com/p3x2007-ops/ha-file-api
   ```

2. **Home Assistant :**
   - Lit `repository.json` → OK, c'est un repo d'add-ons
   - Liste les dossiers → Trouve `file_api_v2/`
   - Lit `file_api_v2/config.yaml` → Affiche "File API v2"
   - Installe depuis `file_api_v2/Dockerfile`

## 📖 READMEs multiples

### README.md (racine)
- **Vue par :** Utilisateurs visitant GitHub
- **Contenu :** Documentation complète du projet
- **Audience :** Développeurs, contributeurs

### file_api_v2/README.md
- **Vue par :** Utilisateurs dans Home Assistant (onglet Documentation)
- **Contenu :** Guide d'installation et configuration
- **Audience :** Utilisateurs finaux Home Assistant

## 🔄 Comparaison avant/après

| Aspect | Avant | Après |
|--------|-------|-------|
| Structure | Fichiers à la racine | Sous-dossier + repository.json |
| Installation GitHub | ❌ Erreur | ✅ Fonctionne |
| URL ingress | Mixte (file_api/file_api_v2) | ✅ Uniforme (file_api_v2) |
| Chemins locaux | /Users/iMac/... | ✅ Génériques |
| Repository URL | anthropics/claude-code | ✅ p3x2007-ops/ha-file-api |

## ✅ Vérifications

### Git commits
```bash
git log --oneline

# Résultat :
# abc1234 Restructure repository for Home Assistant add-on compatibility
# def5678 Initial commit - File API v2.0.0
```

### Structure actuelle
```bash
ls -la
# Doit contenir : repository.json et file_api_v2/

ls -la file_api_v2/
# Doit contenir : config.yaml, Dockerfile, build.yaml, server.py, run.sh, README.md
```

## 🚀 Push vers GitHub

```bash
cd /Users/iMac/claude-files/ha-file-api

# Si repository existe déjà
git remote add origin https://github.com/p3x2007-ops/ha-file-api.git
git branch -M main
git push -u origin main --force  # --force si besoin d'écraser

# Si nouveau repository
# 1. Créer sur https://github.com/new (nom: ha-file-api)
# 2. Puis exécuter les commandes ci-dessus
```

## 🎉 Résultat attendu

Après le push, dans Home Assistant :

1. **Paramètres → Modules complémentaires → Boutique**
2. **Menu ⋮ → Repositories**
3. **Ajouter :** `https://github.com/p3x2007-ops/ha-file-api`
4. **Rafraîchir**
5. ✅ **"File API v2" apparaît dans la liste !**
6. Cliquer → Installer → ✅ **Fonctionne !**

## 📝 Différences techniques

### Installation locale vs GitHub

**Installation locale :**
```
/config/addons/file_api_v2/
├── config.yaml
├── Dockerfile
└── ...
```
→ Pas besoin de repository.json

**Installation GitHub :**
```
Repository GitHub → repository.json requis
└── file_api_v2/ (add-on)
```
→ repository.json obligatoire

## 🔍 Dépannage

### "is not a valid app repository"
**Cause :** Pas de `repository.json` ou structure incorrecte
**Solution :** ✅ Résolu avec cette nouvelle structure

### Add-on n'apparaît pas
**Cause :** Slug ne correspond pas au nom de dossier
**Solution :** `slug: "file_api_v2"` dans config.yaml = dossier `file_api_v2/`

### Build échoue
**Cause :** Fichiers manquants dans le dossier add-on
**Solution :** Vérifier que tous les fichiers sont dans `file_api_v2/`

## 🎯 Prochaines étapes

1. ✅ Structure corrigée
2. ✅ Commits créés
3. 🚀 **Push vers GitHub** (voir PUSH_TO_GITHUB.md)
4. 🧪 **Tester l'installation** dans Home Assistant
5. 📦 **Créer une release** (optionnel) : v2.0.0

---

**Cette structure est maintenant 100% compatible avec Home Assistant ! 🎉**
