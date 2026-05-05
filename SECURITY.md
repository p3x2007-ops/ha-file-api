# Security Policy

🇫🇷 **Français** | 🇬🇧 [English](#english)

---

## 🔒 Versions supportées

| Version | Supportée          |
| ------- | ------------------ |
| 2.x     | ✅ Oui             |
| < 2.0   | ❌ Non             |

## 🐛 Signaler une vulnérabilité

**NE PAS créer d'issue publique pour les vulnérabilités de sécurité.**

### Méthode recommandée

1. Utilisez la fonctionnalité [Security Advisories](https://github.com/p3x2007-ops/ha-file-api/security/advisories) de GitHub
2. Ou envoyez un email privé au mainteneur (voir profil GitHub)

### Informations à fournir

- Description de la vulnérabilité
- Étapes pour reproduire
- Impact potentiel
- Suggestions de correctif (si possible)

### Délai de réponse

- **Confirmation** : sous 48h
- **Analyse** : sous 1 semaine
- **Patch** : selon la gravité (critique < 48h, haute < 1 semaine)

## 🛡️ Bonnes pratiques de sécurité

### Pour les utilisateurs

1. **Utilisez un secret fort** :
   ```bash
   openssl rand -base64 32 | tr -d "=+/" | cut -c1-32
   ```

2. **Mode d'authentification** :
   - Production : `auth_mode: home_assistant` (tokens HA révocables)
   - Automatisation : `auth_mode: api_secret` avec secret fort
   - Évitez `auth_mode: both` en production

3. **Restrictions réseau** :
   - N'exposez PAS l'add-on directement sur Internet
   - Utilisez Home Assistant Cloud (Nabu Casa) ou VPN
   - Activez le pare-feu Home Assistant

4. **Extensions de fichiers** :
   - Limitez aux extensions nécessaires uniquement
   - N'autorisez pas `.php`, `.exe`, `.so`, etc.

5. **Taille de fichiers** :
   - Réglez `max_file_size_mb` au minimum nécessaire
   - Surveillez l'espace disque

6. **Logs** :
   - Activez `log_level: info` pour auditer les accès
   - Surveillez les tentatives d'accès suspects

### Pour les développeurs

- Suivez les principes OWASP Top 10
- Validez toujours les entrées utilisateur
- Échappez les chemins de fichiers
- Pas de logs de secrets
- Revue de code pour les PR sensibles

## 🚨 Vulnérabilités connues

Aucune vulnérabilité active connue.

### Historique

- **v1.x** : Path traversal possible → corrigé dans v2.0
- **v1.x** : Pas de limite de taille → corrigé dans v2.0

---

# English

## 🔒 Supported versions

| Version | Supported          |
| ------- | ------------------ |
| 2.x     | ✅ Yes             |
| < 2.0   | ❌ No              |

## 🐛 Report a vulnerability

**DO NOT create a public issue for security vulnerabilities.**

### Recommended method

1. Use GitHub's [Security Advisories](https://github.com/p3x2007-ops/ha-file-api/security/advisories) feature
2. Or send a private email to the maintainer (see GitHub profile)

### Information to provide

- Vulnerability description
- Steps to reproduce
- Potential impact
- Fix suggestions (if possible)

### Response time

- **Confirmation**: within 48h
- **Analysis**: within 1 week
- **Patch**: depending on severity (critical < 48h, high < 1 week)

## 🛡️ Security best practices

### For users

1. **Use a strong secret**:
   ```bash
   openssl rand -base64 32 | tr -d "=+/" | cut -c1-32
   ```

2. **Authentication mode**:
   - Production: `auth_mode: home_assistant` (revocable HA tokens)
   - Automation: `auth_mode: api_secret` with strong secret
   - Avoid `auth_mode: both` in production

3. **Network restrictions**:
   - DO NOT expose the add-on directly to the Internet
   - Use Home Assistant Cloud (Nabu Casa) or VPN
   - Enable Home Assistant firewall

4. **File extensions**:
   - Limit to necessary extensions only
   - Don't allow `.php`, `.exe`, `.so`, etc.

5. **File size**:
   - Set `max_file_size_mb` to minimum required
   - Monitor disk space

6. **Logs**:
   - Enable `log_level: info` to audit access
   - Monitor suspicious access attempts

### For developers

- Follow OWASP Top 10 principles
- Always validate user input
- Escape file paths
- No logging of secrets
- Code review for sensitive PRs

## 🚨 Known vulnerabilities

No active known vulnerabilities.

### History

- **v1.x**: Path traversal possible → fixed in v2.0
- **v1.x**: No size limit → fixed in v2.0
