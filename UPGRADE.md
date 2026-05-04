# File API v2 - Mise à jour avec authentification

## ⚠️ Problème résolu

**Symptôme :** L'API File API v1.0.0 ne fonctionnait plus avec les tokens Bearer HA, erreur HTTP 401 sur tous les endpoints ingress.

**Cause :** L'ingress Hassio nécessite une session web authentifiée (cookies), pas juste un Bearer token. La v1 comptait uniquement sur l'ingress pour l'auth, mais l'ingress bloque maintenant les requêtes API directes.

**Solution :** File API v2.0.0 vérifie le Bearer token HA **directement dans Flask** avant chaque requête.

## Nouveautés v2.0.0

✅ **Authentification Bearer intégrée**
- Vérifie le token HA sur `http://supervisor/core/api/`
- Header requis : `Authorization: Bearer <votre_token>`
- Endpoint `/health` sans auth (monitoring)

✅ **Meilleure sécurité**
- Token validation à chaque requête
- Logging des tentatives d'auth échouées
- Version visible dans `/health`

✅ **Compatible avec v1**
- Mêmes endpoints
- Même structure JSON
- Même config add-on

## Installation

### Méthode 1 : Nouveau add-on (recommandé)

1. **File Editor** : Créer `/config/addons/file_api_v2/`
2. Télécharger les fichiers depuis GitHub et les uploader dans ce dossier
3. **Paramètres → Modules complémentaires → Boutique → ⋮ → Repositories**
4. Ajouter `/config/addons` si ce n'est pas déjà fait
5. Rafraîchir → **File API v2** → Installer → Démarrer

### Méthode 2 : Remplacer v1 (migration)

1. **Arrêter File API v1** (Paramètres → Modules complémentaires → File API → Arrêter)
2. File Editor : remplacer `/config/addons/file_api/server.py` + `Dockerfile` + `config.yaml`
3. **Paramètres → Modules complémentaires → File API → Reconstruire**
4. Démarrer

## Test

```bash
# Remplacez par votre token HA
HA_TOKEN="YOUR_LONG_LIVED_ACCESS_TOKEN"
HA_URL="https://YOUR_INSTANCE.ui.nabu.casa"

# Health check (no auth)
curl -s "${HA_URL}/api/hassio/ingress/file_api_v2/health"
# → {"status": "healthy", "version": "2.0.0", "auth": "enabled"}

# Lire configuration.yaml (with auth)
curl -s -X POST \
  "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/read" \
  -H "Authorization: Bearer $HA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"path": "configuration.yaml"}'
```

## Différences API

### v1.0.0 (ancienne version)
```bash
# Fonctionnait seulement via ingress web
# Pas de Bearer token requis (auth by ingress)
# ❌ Bloqué maintenant (401)
```

### v2.0.0 (nouvelle version)
```bash
# Fonctionne avec Bearer token HA
# Header Authorization obligatoire
# ✅ Fonctionne maintenant
```

## Endpoints inchangés

- `GET /health` - Health check
- `POST /api/file/read` - Lire fichier
- `POST /api/file/write` - Écrire fichier
- `POST /api/file/delete` - Supprimer fichier
- `POST /api/file/list` - Lister répertoire
- `POST /api/file/exists` - Vérifier existence

## Migration des scripts Claude

Aucun changement nécessaire si vous utilisez déjà le Bearer token dans vos requêtes !

```python
# Avant (v1)
headers = {"Content-Type": "application/json"}  # Pas de token

# Après (v2) 
headers = {
    "Authorization": f"Bearer {HA_TOKEN}",  # Token requis
    "Content-Type": "application/json"
}
```

## Rollback

Si problème, revenez à v1 :
1. Arrêter File API v2
2. Supprimer l'addon File API v2
3. Réinstaller File API v1 (version antérieure de ce repository si disponible)

## Support

Logs : **Paramètres → Modules complémentaires → File API v2 → Journal**

Erreurs communes :
- `401 Missing Authorization header` → Ajouter `-H "Authorization: Bearer <token>"`
- `401 Invalid or expired token` → Générer nouveau token HA
- `403 Path traversal detected` → Path doit être relatif à `/config/`
- `404 File not found` → Vérifier path avec File Editor
