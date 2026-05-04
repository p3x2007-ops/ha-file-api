# 📂 Plan de structure - Installation File API v2

## 🗂️ Vue d'ensemble

```
┌─────────────────────────────────────┐        ┌─────────────────────────────────────┐
│  REPOSITORY GITHUB                  │        │  HOME ASSISTANT                     │
│  ha-file-api/                       │   ───▶ │  /config/addons/                    │
│    (fichiers source)                │        │    file_api_v2/                     │
└─────────────────────────────────────┘        └─────────────────────────────────────┘
```

## 📋 Structure détaillée

### SOURCE (Repository GitHub)

```
ha-file-api/
├── 📄 build.yaml                    ← Fichier 1
├── 📄 config.yaml                   ← Fichier 2 ⭐ IMPORTANT
├── 📄 Dockerfile                    ← Fichier 3
├── 📄 run.sh                        ← Fichier 4
├── 📄 server.py                     ← Fichier 5 ⭐ IMPORTANT
├── 📄 CHANGELOG.md                  ← Documentation (optionnel)
├── 📄 CONFIGURATION.md              ← Documentation (optionnel)
├── 📄 INSTALL.md                    ← Documentation (optionnel)
├── 📄 LICENSE                       ← Documentation (optionnel)
├── 📄 QUICKSTART.md                 ← Documentation (optionnel)
├── 📄 README.md                     ← Documentation (optionnel)
├── 📄 README_GITHUB.txt             ← NE PAS COPIER
├── 📄 SECURITY_CHECK.md             ← NE PAS COPIER
└── 📄 UPGRADE.md                    ← Documentation (optionnel)
```

### DESTINATION (Home Assistant)

```
/config/addons/file_api_v2/
├── 📄 build.yaml                    ← Copier depuis source
├── 📄 config.yaml                   ← Copier depuis source ⭐
├── 📄 Dockerfile                    ← Copier depuis source
├── 📄 run.sh                        ← Copier depuis source
├── 📄 server.py                     ← Copier depuis source ⭐
├── 📄 CHANGELOG.md                  ← Optionnel
├── 📄 CONFIGURATION.md              ← Optionnel
├── 📄 INSTALL.md                    ← Optionnel
├── 📄 LICENSE                       ← Optionnel
├── 📄 QUICKSTART.md                 ← Optionnel
├── 📄 README.md                     ← Optionnel
└── 📄 UPGRADE.md                    ← Optionnel
```

## ✅ Fichiers OBLIGATOIRES (5 fichiers minimum)

Ces fichiers sont **absolument nécessaires** pour que l'addon fonctionne :

| # | Fichier | Taille | Obligatoire | Description |
|---|---------|--------|-------------|-------------|
| 1 | `build.yaml` | 354 B | ✅ OUI | Config build multi-arch |
| 2 | `config.yaml` | 966 B | ✅ OUI | Config addon + auth modes |
| 3 | `Dockerfile` | 426 B | ✅ OUI | Image Docker |
| 4 | `run.sh` | 476 B | ✅ OUI | Script démarrage |
| 5 | `server.py` | 11 KB | ✅ OUI | Code Python API |

**Total minimum : 5 fichiers, ~13 KB**

## 📚 Fichiers OPTIONNELS (Documentation)

Ces fichiers améliorent l'expérience mais ne sont pas requis pour le fonctionnement :

| Fichier | Taille | Utilité |
|---------|--------|---------|
| `README.md` | 6.3 KB | Documentation principale |
| `QUICKSTART.md` | 4.5 KB | Guide rapide 5 min |
| `CONFIGURATION.md` | 7.5 KB | Guide modes auth |
| `CHANGELOG.md` | 2.7 KB | Historique versions |
| `INSTALL.md` | 5.3 KB | Guide installation détaillé |
| `UPGRADE.md` | 3.7 KB | Migration v1→v2 |
| `LICENSE` | 1.1 KB | Licence MIT |

## ❌ Fichiers à NE PAS COPIER

| Fichier | Raison |
|---------|--------|
| `README_GITHUB.txt` | Guide publication GitHub (usage local) |
| `SECURITY_CHECK.md` | Rapport sécurité (usage local) |

## 🎯 Mapping fichier par fichier

### Obligatoires

```
SOURCE                                          DESTINATION
──────────────────────────────────────────────────────────────────────
ha-file-api/                                    /config/addons/
  (repository)                                    file_api_v2/
    ├── build.yaml                  ────────▶       ├── build.yaml
    ├── config.yaml                 ────────▶       ├── config.yaml
    ├── Dockerfile                  ────────▶       ├── Dockerfile
    ├── run.sh                      ────────▶       ├── run.sh
    └── server.py                   ────────▶       └── server.py
```

### Optionnels (documentation)

```
SOURCE                                          DESTINATION
──────────────────────────────────────────────────────────────────────
ha-file-api/                                    /config/addons/
  (repository)                                    file_api_v2/
    ├── CHANGELOG.md                ────────▶       ├── CHANGELOG.md
    ├── CONFIGURATION.md            ────────▶       ├── CONFIGURATION.md
    ├── INSTALL.md                  ────────▶       ├── INSTALL.md
    ├── LICENSE                     ────────▶       ├── LICENSE
    ├── QUICKSTART.md               ────────▶       ├── QUICKSTART.md
    ├── README.md                   ────────▶       ├── README.md
    └── UPGRADE.md                  ────────▶       └── UPGRADE.md
```

## 📝 Instructions étape par étape

### Option A : Installation minimale (5 fichiers)

**Étape 1 : Télécharger le repository**
```bash
git clone https://github.com/p3x2007-ops/ha-file-api.git
# Ou télécharger le ZIP depuis GitHub
```

**Étape 2 : Sélectionner les 5 fichiers obligatoires**
- ✅ `build.yaml`
- ✅ `config.yaml`
- ✅ `Dockerfile`
- ✅ `run.sh`
- ✅ `server.py`

**Étape 3 : Dans Home Assistant**
1. Ouvrir **File Editor**
2. Créer dossier `/config/addons/file_api_v2/`
3. Glisser les 5 fichiers dans ce dossier
4. ✅ Terminé !

### Option B : Installation complète (12 fichiers)

**Étape 1 : Télécharger le repository**
```bash
git clone https://github.com/p3x2007-ops/ha-file-api.git
# Ou télécharger le ZIP depuis GitHub
```

**Étape 2 : Sélectionner TOUS les fichiers SAUF**
- ❌ `README_GITHUB.txt`
- ❌ `SECURITY_CHECK.md`

**Étape 3 : Dans Home Assistant**
1. Ouvrir **File Editor**
2. Créer dossier `/config/addons/file_api_v2/`
3. Glisser tous les fichiers sélectionnés
4. ✅ Terminé !

## 🖼️ Vue arborescente finale

Après installation dans Home Assistant, vous devriez voir :

```
📁 /config/
├── 📁 addons/
│   └── 📁 file_api_v2/              ← NOUVEAU DOSSIER
│       ├── 📄 build.yaml
│       ├── 📄 config.yaml           ⭐ Config addon
│       ├── 📄 Dockerfile
│       ├── 📄 run.sh
│       ├── 📄 server.py             ⭐ Code API
│       └── 📄 [docs optionnelles]
├── 📁 automations.yaml
├── 📁 configuration.yaml
└── 📁 www/
```

## ✅ Vérification post-installation

### Dans File Editor
```
Navigation : /config/addons/file_api_v2/

Vous devez voir :
✅ 5 fichiers minimum
✅ config.yaml (~966 bytes)
✅ server.py (~11 KB)
```

### Dans Home Assistant
```
Paramètres → Modules complémentaires → Boutique → ⋮ → Repositories
→ Ajouter : /config/addons
→ Rafraîchir
→ Chercher "File API v2"
```

## 🎨 Aide visuelle - Copier/Coller

### Sélection des fichiers

```
┌─────────────────────────────────────────────┐
│  ha-file-api/                               │
├─────────────────────────────────────────────┤
│  ☑️ build.yaml              354 B           │
│  ☑️ config.yaml             966 B    ⭐     │
│  ☑️ Dockerfile              426 B           │
│  ☑️ run.sh                  476 B           │
│  ☑️ server.py               11 KB    ⭐     │
│  ─────────────────────────────────────────  │
│  ☑️ CHANGELOG.md            2.7 KB          │
│  ☑️ CONFIGURATION.md        7.5 KB          │
│  ☑️ INSTALL.md              5.3 KB          │
│  ☑️ LICENSE                 1.1 KB          │
│  ☑️ QUICKSTART.md           4.5 KB          │
│  ☑️ README.md               6.3 KB          │
│  ☑️ UPGRADE.md              3.7 KB          │
│  ─────────────────────────────────────────  │
│  ☐ README_GITHUB.txt        ❌ Ne pas copier│
│  ☐ SECURITY_CHECK.md        ❌ Ne pas copier│
└─────────────────────────────────────────────┘
```

### Upload dans File Editor

```
┌─────────────────────────────────────────────┐
│  File Editor - /config/addons/file_api_v2/ │
├─────────────────────────────────────────────┤
│  📁 file_api_v2/          ← Nouveau dossier │
│                                              │
│  [Glisser les fichiers ici]                 │
│                                              │
│  Ou cliquer sur "Upload files" →            │
└─────────────────────────────────────────────┘
```

## 🚀 Après l'upload

1. **Ajouter le repository local** (si pas déjà fait)
   - Menu ⋮ → Repositories
   - Ajouter : `/config/addons`

2. **Rafraîchir la page**
   - F5 ou bouton Rafraîchir

3. **Chercher l'addon**
   - "File API v2" devrait apparaître dans "Local add-ons"

4. **Installer**
   - Cliquer → Installer → Attendre 1-2 min

5. **Configurer**
   - Onglet Configuration
   - Définir `auth_mode` et `api_secret`
   - Sauvegarder

6. **Démarrer**
   - Bouton "DÉMARRER"
   - ✅ Prêt !

## 💡 Conseil

**Pour une première installation, je recommande l'Option A (5 fichiers minimum).**

Vous pourrez toujours ajouter la documentation plus tard en uploadant les fichiers `.md` supplémentaires.

**Les fichiers de documentation peuvent être ajoutés APRÈS l'installation** sans avoir besoin de reconstruire l'addon.
