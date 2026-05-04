# 🚀 Démarrage rapide - File API v2

Guide en **5 minutes** pour installer et configurer File API v2.

## Étape 1 : Installer l'addon (2 min)

### Via File Editor

1. **Créer le dossier** `/config/addons/file_api_v2/`

2. **Uploader les fichiers** depuis votre ordinateur :
   - `config.yaml`
   - `Dockerfile`
   - `build.yaml`
   - `server.py`
   - `run.sh`

3. **Ajouter le repository local**
   - Paramètres → Modules complémentaires → Boutique → ⋮ → Repositories
   - Ajouter : `/config/addons`
   - Rafraîchir la page

4. **Installer**
   - Chercher "File API v2"
   - Cliquer → Installer
   - Attendre la fin (1-2 min)

## Étape 2 : Configurer l'authentification (1 min)

### Option A : API Secret (Recommandé pour Claude)

1. **Générer un secret fort** (Terminal) :
   ```bash
   openssl rand -base64 32 | tr -d "=+/" | cut -c1-32
   ```
   
   Exemple de résultat : `K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA`

2. **Configurer l'addon** :
   - Onglet "Configuration"
   - Modifier :
     ```yaml
     auth_mode: api_secret
     api_secret: "K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA"
     ```
   - **Sauvegarder**

3. **Démarrer l'addon** → Bouton "DÉMARRER"

### Option B : Token Home Assistant

1. **Créer un token HA** :
   - Profil (bas gauche) → Tokens d'accès de longue durée
   - **Créer un token** (nom : "File API Claude")
   - **Copier le token**

2. **Laisser la config par défaut** :
   ```yaml
   auth_mode: home_assistant
   api_secret: ""
   ```

3. **Démarrer l'addon**

## Étape 3 : Tester (1 min)

### Avec API Secret

```bash
HA_URL="https://YOUR_INSTANCE.ui.nabu.casa"
SECRET="K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA"

# Health check
curl -s "${HA_URL}/api/hassio/ingress/file_api_v2/health"

# Lister /config/www/
curl -s -X POST "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/list" \
  -H "Authorization: Bearer ${SECRET}" \
  -H "Content-Type: application/json" \
  -d '{"path": "www"}'
```

### Avec Token HA

```bash
HA_URL="https://YOUR_INSTANCE.ui.nabu.casa"
HA_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# Lister /config/www/
curl -s -X POST "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/list" \
  -H "Authorization: Bearer ${HA_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"path": "www"}'
```

**✅ Si vous voyez `"success": true` → L'addon fonctionne !**

## Étape 4 : Utiliser avec Claude Code (1 min)

### Sauvegarder le secret dans Claude

1. Ouvrir une conversation avec Claude Code

2. Donner le secret :
   ```
   Mon File API secret est : K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA
   
   URL Home Assistant : https://YOUR_INSTANCE.ui.nabu.casa
   ```

3. Claude peut maintenant automatiser les modifications :
   ```
   "Mets à jour la card Dolce Gusto pour changer la couleur"
   ```

Claude va :
1. ✅ Télécharger `dolce-gusto-card.js` via File API
2. ✅ Modifier le fichier localement
3. ✅ Uploader automatiquement via File API
4. ✅ Terminé - Aucune action manuelle !

## 📊 Vérification

### Dans les logs de l'addon

**Paramètres → Modules complémentaires → File API v2 → Journal**

Vous devriez voir :
```
Starting File API Server v2.0.0 (with authentication)
Base path: /config
Max file size: 10 MB
Authentication mode: api_secret
API Secret configured: K7mP9nQ2...
```

### Health check

```bash
curl -s "${HA_URL}/api/hassio/ingress/file_api_v2/health"
```

**Résultat attendu :**
```json
{
  "status": "healthy",
  "version": "2.0.0",
  "auth_mode": "api_secret",
  "api_secret_configured": true
}
```

## ❓ Problèmes fréquents

### "Invalid or expired token"

**Cause :** Token incorrect ou mode mal configuré.

**Solution :**
1. Vérifier le mode dans `/health`
2. Si `api_secret` → Utiliser votre secret
3. Si `home_assistant` → Utiliser token HA

### "API Secret NOT configured"

**Cause :** Mode `api_secret` mais champ vide.

**Solution :**
1. Ouvrir configuration addon
2. Remplir `api_secret: "votre_secret"`
3. Sauvegarder et redémarrer

### Addon ne démarre pas

**Cause :** Erreur dans Dockerfile ou dépendances manquantes.

**Solution :**
1. Vérifier les logs : Journal → onglet
2. Reconstruire : Options → Rebuild
3. Si erreur persiste, copier logs et ouvrir issue GitHub

## 🎉 C'est prêt !

File API v2 est maintenant opérationnel. Claude Code peut automatiser 100% des modifications de vos fichiers Home Assistant.

**Prochaines étapes :**
- 📖 Lire [CONFIGURATION.md](CONFIGURATION.md) pour options avancées
- 🔒 Lire [SECURITY_CHECK.md](SECURITY_CHECK.md) pour bonnes pratiques
- 🚀 Tester avec une vraie modification via Claude

**Besoin d'aide ?** Ouvrez une issue sur GitHub.
