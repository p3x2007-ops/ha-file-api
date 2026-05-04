# Configuration File API v2

## 🔐 Modes d'authentification

File API v2 offre **3 modes d'authentification** configurables lors de l'installation.

### Mode 1 : Home Assistant Token (Défaut)

**Configuration :**
```yaml
auth_mode: home_assistant
api_secret: ""  # Laissez vide
```

**Utilisation :**
```bash
# Générez un Long-Lived Access Token dans HA
# Profil → Tokens d'accès de longue durée → Créer un token

curl -X POST "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/read" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{"path": "configuration.yaml"}'
```

**✅ Avantages :**
- Sécurité maximale (token HA natif)
- Révocation facile dans HA
- Expire si défini

**❌ Inconvénients :**
- Token long et complexe
- Nécessite régénération si révoqué

---

### Mode 2 : API Secret personnalisé (Recommandé pour Claude)

**Configuration :**
```yaml
auth_mode: api_secret
api_secret: "mon_secret_super_securise_123"  # Définissez votre secret
```

**Utilisation :**
```bash
# Utilisez votre secret comme Bearer token
curl -X POST "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/read" \
  -H "Authorization: Bearer mon_secret_super_securise_123" \
  -H "Content-Type: application/json" \
  -d '{"path": "configuration.yaml"}'
```

**✅ Avantages :**
- Token simple et mémorisable
- Pas de dépendance à HA
- Parfait pour scripts automatisés

**❌ Inconvénients :**
- Moins sécurisé qu'un token HA
- Pas de révocation facile (modifier config addon)

**💡 Recommandation :** 
Générez un secret aléatoire fort :
```bash
# Générer un secret de 32 caractères
openssl rand -base64 32 | tr -d "=+/" | cut -c1-32
# Ex: K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA
```

---

### Mode 3 : Les deux (Both)

**Configuration :**
```yaml
auth_mode: both
api_secret: "mon_secret_123"
```

**Utilisation :**
Accepte **soit** le token HA **soit** votre API secret.

**✅ Avantages :**
- Maximum de flexibilité
- Token HA pour usage ponctuel
- API secret pour automatisation

**❌ Inconvénients :**
- Surface d'attaque plus grande
- Configuration plus complexe

---

## ⚙️ Configuration complète

### Interface addon (après installation)

1. **Paramètres → Modules complémentaires → File API v2**
2. Onglet **Configuration**
3. Modifier les valeurs :

```yaml
# Mode d'authentification
auth_mode: api_secret  # home_assistant | api_secret | both

# Secret API (si mode api_secret ou both)
api_secret: "VOTRE_SECRET_ICI"

# Niveau de logs
log_level: info  # debug, info, warning, error

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
max_file_size_mb: 10
```

4. **Sauvegarder**
5. **Redémarrer l'addon**

---

## 🚀 Guide d'installation configuré

### Étape 1 : Installer l'addon

(Suivre INSTALL.md)

### Étape 2 : Configurer l'authentification

**Pour usage avec Claude Code (recommandé) :**

1. Ouvrir la configuration de l'addon
2. Définir :
   ```yaml
   auth_mode: api_secret
   api_secret: "K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA"  # Générez le vôtre !
   ```
3. Sauvegarder et redémarrer

**Pour usage avec scripts Home Assistant :**

1. Laisser la config par défaut :
   ```yaml
   auth_mode: home_assistant
   api_secret: ""
   ```
2. Créer un token HA : **Profil → Tokens d'accès de longue durée**

### Étape 3 : Tester

```bash
# Health check (voir le mode configuré)
curl -s "${HA_URL}/api/hassio/ingress/file_api_v2/health"

# Résultat :
{
  "status": "healthy",
  "version": "2.0.0",
  "auth_mode": "api_secret",
  "api_secret_configured": true
}
```

```bash
# Test avec votre secret
curl -s -X POST "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/list" \
  -H "Authorization: Bearer K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA" \
  -H "Content-Type: application/json" \
  -d '{"path": "www"}'
```

---

## 🔒 Sécurité

### Bonnes pratiques

**✅ À FAIRE :**
- Utilisez un secret fort (32+ caractères aléatoires)
- Ne partagez jamais votre secret
- Changez le secret régulièrement
- Utilisez HTTPS (Nabu Casa ou reverse proxy)
- Limitez l'accès réseau à l'addon

**❌ À NE PAS FAIRE :**
- Secret simple comme "password123"
- Commiter le secret dans Git
- Utiliser le même secret partout
- Exposer l'addon sur Internet sans HTTPS

### Générer un secret fort

**Option 1 : OpenSSL (Terminal Mac/Linux)**
```bash
openssl rand -base64 32 | tr -d "=+/" | cut -c1-32
```

**Option 2 : Python**
```python
import secrets
print(secrets.token_urlsafe(32))
```

**Option 3 : Site web (si vous n'avez pas accès au terminal)**
https://passwordsgenerator.net/ (32 caractères, alphanumerique)

---

## 📊 Comparaison des modes

| Critère | Home Assistant | API Secret | Both |
|---------|----------------|------------|------|
| Sécurité | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Simplicité setup | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Automatisation | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Révocation | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |

**Recommandation par cas d'usage :**

| Usage | Mode recommandé |
|-------|-----------------|
| Claude Code automatisé | `api_secret` |
| Scripts HA ponctuels | `home_assistant` |
| Environnement partagé | `home_assistant` |
| CI/CD pipelines | `api_secret` |
| Maximum sécurité | `home_assistant` |
| Maximum simplicité | `api_secret` |

---

## 🐛 Troubleshooting

### Erreur : HTTP 401 "Invalid or expired token"

**Cause :** Token incorrect ou mode d'auth mal configuré.

**Solution :**
1. Vérifier le mode : `curl ${HA_URL}/api/hassio/ingress/file_api_v2/health`
2. Si `auth_mode: api_secret` → Utiliser votre secret
3. Si `auth_mode: home_assistant` → Utiliser token HA
4. Vérifier que `api_secret_configured: true` si mode api_secret

### Erreur : "API Secret NOT configured"

**Cause :** Mode `api_secret` mais champ vide.

**Solution :**
1. Ouvrir configuration addon
2. Remplir `api_secret: "votre_secret"`
3. Sauvegarder et redémarrer

### Le token HA ne fonctionne plus

**Cause :** Token révoqué ou expiré.

**Solution :**
1. Profil HA → Tokens d'accès de longue durée
2. Supprimer l'ancien token
3. Créer un nouveau token
4. Mettre à jour vos scripts

---

## 💡 Exemples d'usage

### Avec Claude Code

1. Configurer `api_secret` dans l'addon
2. Sauvegarder le secret dans la mémoire Claude :

```bash
# Dans une conversation avec Claude :
"Mon API secret File API est : K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA"
```

3. Claude peut ensuite automatiser :
```bash
curl -X POST "${HA_URL}/api/hassio/ingress/file_api_v2/api/file/write" \
  -H "Authorization: Bearer K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA" \
  -H "Content-Type: application/json" \
  -d '{"path": "www/dolce-gusto-card.js", "content": "..."}'
```

### Avec scripts Node.js

```javascript
const axios = require('axios');

const fileAPI = axios.create({
  baseURL: 'https://YOUR_INSTANCE.ui.nabu.casa/api/hassio/ingress/file_api_v2',
  headers: {
    'Authorization': 'Bearer K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA',
    'Content-Type': 'application/json'
  }
});

// Lire configuration.yaml
const config = await fileAPI.post('/api/file/read', {
  path: 'configuration.yaml'
});
console.log(config.data.content);
```

### Avec shell_command HA

```yaml
# configuration.yaml
shell_command:
  backup_config: >
    curl -X POST "http://localhost:8100/api/file/read" 
    -H "Authorization: Bearer K7mP9nQ2wX5tY8zR4vL1cH6jN3bM0sA"
    -H "Content-Type: application/json"
    -d '{"path": "configuration.yaml"}' > /config/backups/config_$(date +%Y%m%d).yaml
```
