# 🔍 Guide de débogage - Add-on invisible dans Home Assistant

## ✅ Structure validée

Votre repository est **100% conforme** :
- ✓ repository.yaml à la racine
- ✓ slug correct : `file-api`
- ✓ Icônes présentes (256x256 et 512x512)
- ✓ Tous les fichiers requis
- ✓ Poussé sur GitHub

## 🎯 Étapes de débogage

### Étape 1 : Nettoyer le cache HA (CRITIQUE)

**Home Assistant met en cache les repositories.** Il faut forcer le rechargement :

1. **Ouvrir Home Assistant** → Paramètres → Modules complémentaires
2. **Boutique** → Menu **⋮** (haut droite) → **Dépôts personnalisés**
3. **Trouver** : `https://github.com/p3x2007-ops/ha-file-api`
4. **Cliquer sur les 3 points** à droite du repository
5. **SUPPRIMER** complètement
6. **Redémarrer le Supervisor** :
   - Paramètres → Système → **Redémarrer** → Sélectionner **"Supervisor"**
7. **Attendre 1 minute** après le redémarrage
8. **Retourner** à Boutique → Menu ⋮ → Dépôts personnalisés
9. **AJOUTER** : `https://github.com/p3x2007-ops/ha-file-api`
10. **Catégorie** : Automation
11. **Attendre 30-60 secondes**
12. **Retourner** à la boutique principale

### Étape 2 : Vérifier les logs du Supervisor

Si l'add-on n'apparaît toujours pas :

1. **Paramètres** → **Système** → **Journaux**
2. **Sélectionner** : **"Supervisor"** (dans le menu déroulant)
3. **Rechercher** (Ctrl+F) :
   - `ha-file-api`
   - `file-api`
   - `p3x2007-ops`
   - `error`
   - `warning`

**Copier toute erreur trouvée** - elle indiquera le problème exact.

### Étape 3 : Vérifier l'accès GitHub depuis HA

Le Supervisor doit pouvoir accéder à GitHub. Tester :

1. **Terminal SSH ou Console** dans HA
2. Exécuter :
   ```bash
   curl -I https://github.com/p3x2007-ops/ha-file-api
   ```
3. Devrait retourner **HTTP 200**

Si erreur réseau → problème de connectivité ou pare-feu.

### Étape 4 : Vérifier que GitHub sert bien les fichiers

Dans un navigateur :
- https://github.com/p3x2007-ops/ha-file-api/blob/main/repository.yaml
- https://github.com/p3x2007-ops/ha-file-api/blob/main/file-api/config.yaml
- https://github.com/p3x2007-ops/ha-file-api/blob/main/file-api/icon.png

Tous doivent s'afficher correctement.

### Étape 5 : Essayer avec raw.githubusercontent.com

Parfois HA a des problèmes avec les URLs GitHub. Tester :

```bash
curl https://raw.githubusercontent.com/p3x2007-ops/ha-file-api/main/repository.yaml
```

Devrait afficher le contenu YAML.

## 🐛 Problèmes connus et solutions

### Problème : "Repository not found"
**Cause** : GitHub repository privé ou URL incorrecte  
**Solution** : Vérifier que le repo est **public** sur GitHub

### Problème : "Invalid repository structure"
**Cause** : Fichier manquant ou mal formaté  
**Solution** : Exécuter `bash DIAGNOSTIC.sh` et corriger

### Problème : Cache HA persistant
**Cause** : HA ne recharge pas le repository  
**Solution** : Redémarrer le **Supervisor** (pas Home Assistant complet)

### Problème : Pas d'erreur dans les logs mais toujours invisible
**Causes possibles** :
1. **Mauvaise branche** : HA lit `main` par défaut, vérifier que c'est votre branche par défaut
2. **Délai de propagation** : Attendre 2-3 minutes après l'ajout
3. **Bug HA** : Redémarrer Home Assistant complètement

## 🔧 Commandes de diagnostic HA

Si vous avez accès au terminal/SSH :

```bash
# Lister tous les repositories connus
ha addons repositories list

# Recharger les repositories
ha addons reload

# Voir info d'un repository spécifique
ha addons repositories info <slug>

# Forcer mise à jour
ha supervisor update
```

## 📞 Si rien ne marche

**Dernière option** : Tester avec un repository d'exemple officiel d'abord :

1. Ajouter : `https://github.com/home-assistant/addons-example`
2. Si celui-ci apparaît → problème spécifique à votre repo
3. Si celui-ci n'apparaît pas → problème HA général

## 🎬 Action immédiate recommandée

**FAITES CECI MAINTENANT** :

1. ✅ Redémarrer le **Supervisor** (pas HA complet)
2. ✅ Supprimer et ré-ajouter le repository **après** le redémarrage
3. ✅ Vérifier les **logs du Supervisor** pour toute erreur
4. ✅ **Attendre 2 minutes** complètes avant de vérifier la boutique

---

**Note** : La structure du repository est correcte. Le problème vient du cache HA ou d'un problème de connectivité/logs côté Supervisor.
