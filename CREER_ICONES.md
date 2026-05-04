# 🎨 Création des icônes pour l'add-on

## Fichiers requis

Placez ces fichiers dans `/file_api_v2/` :

### 1. icon.png
- **Taille** : 128x128 pixels minimum (recommandé : 256x256)
- **Format** : PNG avec transparence
- **Usage** : Icône principale de l'add-on dans la liste

### 2. logo.png (optionnel)
- **Taille** : 256x256 pixels ou plus
- **Format** : PNG avec transparence
- **Usage** : Logo affiché en haut de la page de l'add-on

## Thème suggéré pour File API

**Concept visuel** : Document/Fichier + API/Réseau

### Idées de design :
- 📁 Dossier avec symbole API (crochets `{ }`)
- 🔌 Fichier avec prise/connecteur
- 📄 Document avec icône réseau
- 🗂️ Serveur de fichiers stylisé

### Couleurs recommandées :
- **Primaire** : Bleu (#2196F3 - couleur HA standard)
- **Secondaire** : Vert (#4CAF50 - pour "actif/connecté")
- **Accent** : Orange (#FF9800 - pour "API/données")

## Outils pour créer les icônes

### En ligne (gratuit) :
1. **Canva** (canva.com) - Templates d'icônes
2. **Figma** (figma.com) - Design professionnel
3. **GIMP** (gimp.org) - Logiciel gratuit

### IA génération :
1. **DALL-E** / **Midjourney** - Générer une icône
2. **Prompt suggéré** :
   ```
   Simple flat icon for a file API application, 
   minimalist design, blue and green colors, 
   folder with API brackets symbol, 
   transparent background, 256x256 pixels
   ```

## Installation rapide

### Option 1 : Télécharger des icônes libres
- [Flaticon](https://www.flaticon.com) - Rechercher "file api" ou "folder network"
- [Icons8](https://icons8.com) - Style "material design"
- Redimensionner à 256x256 avec un outil en ligne

### Option 2 : Icône placeholder temporaire
Créez une icône simple avec un fond de couleur et du texte :
- Fond bleu (#2196F3)
- Texte blanc "API"
- 256x256 pixels

## Après création

1. Placez `icon.png` dans `/file_api_v2/`
2. (Optionnel) Placez `logo.png` dans `/file_api_v2/`
3. Commitez et pushez :
   ```bash
   git add file_api_v2/icon.png file_api_v2/logo.png
   git commit -m "Ajout des icônes de l'add-on"
   git push
   ```
4. Dans Home Assistant : Rafraîchissez le repository
5. L'icône devrait maintenant apparaître !

## Vérification

Une fois les icônes ajoutées, votre structure devrait ressembler à :

```
file_api_v2/
├── icon.png          ← NOUVEAU
├── logo.png          ← NOUVEAU (optionnel)
├── config.yaml
├── README.md
├── Dockerfile
├── build.yaml
├── run.sh
└── server.py
```
