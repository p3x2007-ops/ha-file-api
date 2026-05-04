# Changelog - File API

## v2.0.0 (2026-05-04)

### 🎉 Nouvelles fonctionnalités

**Authentification configurable**
- ✨ Ajout de 3 modes d'authentification : `home_assistant`, `api_secret`, `both`
- ✨ Configuration via UI addon (champ `api_secret` et `auth_mode`)
- ✨ API Secret personnalisé pour automatisation simple
- ✨ Support simultané token HA et API secret en mode `both`

**Amélioration monitoring**
- ✨ Endpoint `/health` enrichi : affiche `auth_mode` et `api_secret_configured`
- ✨ Logs de démarrage détaillés avec configuration auth
- ✨ Warning si API secret non configuré en mode `api_secret`

### 🔒 Sécurité

- ✅ Validation token HA inchangée (via `http://supervisor/core/api`)
- ✅ API Secret utilise comparaison stricte (`==`)
- ✅ Champ `api_secret` de type `password` dans config (masqué dans UI)

### 📝 Documentation

- 📖 Nouveau : `CONFIGURATION.md` - Guide complet des modes d'auth
- 📖 Nouveau : `QUICKSTART.md` - Installation en 5 minutes
- 📖 Nouveau : `CHANGELOG.md` - Historique des versions
- 📖 Mise à jour : `README.md` - Section authentification
- 📖 Mise à jour : `UPGRADE.md` - Migration v1 → v2

### 🔧 Modifications techniques

**config.yaml**
- Ajout option `api_secret` (type password)
- Ajout option `auth_mode` (choix : home_assistant, api_secret, both)

**server.py**
- Fonction `verify_api_secret(token)` pour validation secret
- Fonction `verify_token(token)` dispatcher selon `auth_mode`
- Variables globales `API_SECRET` et `AUTH_MODE` chargées depuis options
- Health endpoint retourne `auth_mode` et `api_secret_configured`

### 🐛 Corrections

- Aucun bug corrigé (nouvelle version majeure)

### ⚠️ Breaking Changes

**Aucun** - File API v2 est **rétrocompatible** avec v1 :
- Mode `home_assistant` (défaut) fonctionne exactement comme v1
- Pas de changement dans les endpoints API
- Pas de changement dans le format des requêtes/réponses

### 📦 Migration depuis v1

Voir [UPGRADE.md](UPGRADE.md) pour le guide complet.

**TL;DR :**
1. Remplacer `file_api` v1 par `file_api_v2`
2. Laisser config par défaut (mode `home_assistant`) ou configurer `api_secret`
3. Tester

---

## v1.0.0 (2026-04-30)

### 🎉 Version initiale

**Fonctionnalités**
- ✅ API REST complète (read, write, delete, list, exists)
- ✅ Authentification via token HA uniquement
- ✅ Protection path traversal
- ✅ Limite taille fichiers configurable
- ✅ Whitelist extensions configurables
- ✅ Logging complet
- ✅ Support ingress Hassio

**Limitations**
- ❌ Token HA obligatoire (problème ingress avec curl)
- ❌ Pas d'API secret personnalisé
- ❌ Ingress requiert session web (cookies)

**Raison v2**
- Ingress bloque requêtes API directes (HTTP 401)
- Besoin d'auth Bearer simple pour automatisation
