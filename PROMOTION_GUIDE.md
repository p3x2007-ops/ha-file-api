# Guide de Promotion - File API v2

Ce guide vous aide à augmenter la visibilité de votre add-on.

## ✅ Actions déjà réalisées

- [x] Repository configuré avec description et topics
- [x] README avec badges (release, stars, license)
- [x] Documentation complète bilingue (FR/EN)
- [x] Fichiers communautaires (CONTRIBUTING, SECURITY, CODE_OF_CONDUCT)
- [x] Templates GitHub (Issues, PR)
- [x] Workflow CI/CD (validation automatique)
- [x] GitHub Discussions activées
- [x] Release v2.0.0 publiée
- [x] Licence MIT
- [x] FUNDING.yml (sponsorship)

## 🎯 Prochaines étapes - Publication

### 1. Home Assistant Community Forum

**Où** : https://community.home-assistant.io/c/third-party/custom-addons/87

**Titre suggéré** :
```
[Add-on] File API v2 - Secure REST API for Configuration Management
```

**Contenu** : Utilisez `COMMUNITY_POST.md` comme base

**Tags** : `addon`, `api`, `automation`, `claude-code`

### 2. Reddit r/homeassistant

**Où** : https://reddit.com/r/homeassistant

**Titre suggéré** :
```
[Release] File API v2 - REST API for HA Config Management (Claude Code Integration)
```

**Format** :
- Lead with the problem it solves
- Bullet points for features
- Installation link
- Screenshot or demo GIF

**Tag** : `[Release]` ou `[Project Showcase]`

### 3. Home Assistant Discord

**Où** : https://discord.gg/home-assistant

**Canal** : `#third-party-addons`

**Message court** :
```
🎉 File API v2 released! Secure REST API for reading/writing HA config files.
Perfect for Claude Code automation. 3 auth modes, path protection, bilingual docs.
⭐ https://github.com/p3x2007-ops/ha-file-api
```

### 4. Twitter/X

```
🚀 Launched File API v2 for #HomeAssistant!

Secure REST API for config file management
✅ 3 auth modes
✅ Path protection  
✅ Perfect for @AnthropicAI Claude Code automation

⭐ https://github.com/p3x2007-ops/ha-file-api

#smarthome #homeautomation #opensource
```

### 5. Awesome Home Assistant

**Où** : https://github.com/frenck/awesome-home-assistant

**Action** : Soumettre PR pour ajouter dans section "Add-ons"

**Format** :
```markdown
- [File API v2](https://github.com/p3x2007-ops/ha-file-api) - Secure REST API for configuration file management.
```

### 6. HACS (Home Assistant Community Store)

**Attention** : HACS est pour les **intégrations custom**, pas les add-ons.

Les add-ons sont installés via **repository GitHub** directement (déjà fait ✅).

### 7. Blog/Medium Article (optionnel)

**Titre** : "Automate Your Home Assistant Config with Claude Code and File API v2"

**Contenu** :
1. The problem: Manual config editing
2. The solution: File API v2
3. Installation guide
4. Claude Code integration example
5. Security considerations
6. Conclusion + GitHub link

**Plateformes** :
- Medium
- Dev.to
- Hashnode
- Votre blog personnel

## 📊 Suivi de la visibilité

### Métriques à surveiller

```bash
# GitHub stars
gh repo view p3x2007-ops/ha-file-api --json stargazersCount

# Forks
gh repo view p3x2007-ops/ha-file-api --json forkCount

# Issues/Discussions
gh issue list --repo p3x2007-ops/ha-file-api
gh api repos/p3x2007-ops/ha-file-api/discussions

# Traffic (nécessite admin access)
gh api repos/p3x2007-ops/ha-file-api/traffic/views
gh api repos/p3x2007-ops/ha-file-api/traffic/clones
```

### GitHub Insights

Accédez à : https://github.com/p3x2007-ops/ha-file-api/graphs/traffic

Surveillez :
- Vues du repository
- Visiteurs uniques
- Clones Git
- Referring sites

## 🎨 Améliorations visuelles (optionnel)

### 1. Logo/Icon personnalisé

Créez un logo 512×512px pour votre add-on et ajoutez-le dans `file_api_v2/icon.png`

### 2. Screenshots

Ajoutez dans README.md :
- Capture d'écran de l'UI addon
- Exemple de réponse API
- Dashboard Claude Code utilisant l'API

### 3. Demo GIF

Créez un GIF animé montrant :
1. Installation de l'add-on
2. Configuration
3. Test d'un endpoint avec curl

Outils : Peek (Linux), LICEcap (Win/Mac), Kap (Mac)

### 4. Social Preview Image

Créez une image 1200×630px pour l'aperçu social GitHub :

**Contenu** :
- Titre : "File API v2"
- Sous-titre : "Secure REST API for Home Assistant"
- Logo HA + Claude Code
- URL : github.com/p3x2007-ops/ha-file-api

**Ajout** : Repository Settings → Social preview → Upload image

## 🤝 Engagement communautaire

### Répondez rapidement aux :
- ⭐ Issues GitHub
- 💬 Discussions
- 📝 Pull Requests
- 💭 Comments sur forums/Reddit

### Remerciez les contributeurs :
- Stars
- Forks
- Pull Requests
- Bug reports

### Mettez à jour régulièrement :
- Releases avec changelog
- Réponse aux feature requests
- Documentation

## 📈 SEO GitHub

Votre repository est déjà optimisé avec :
- ✅ Description claire et concise
- ✅ 12 topics pertinents
- ✅ Homepage URL
- ✅ README complet avec badges
- ✅ Licence MIT
- ✅ Documentation complète

### Amélioration continue :

1. **Encouragez les stars** : Ajoutez dans README :
   ```markdown
   ⭐ Star the repo if you find it useful!
   ```

2. **Demandez du feedback** : Créez une discussion "Feedback & Feature Requests"

3. **Showcases utilisateurs** : Encouragez les users à partager leur usage

4. **Vidéo tutorial** : YouTube tutorial = grande visibilité

## 🎁 Bonus : Badge personnalisés

Ajoutez dans README.md :

```markdown
<!-- Installations -->
![GitHub downloads](https://img.shields.io/github/downloads/p3x2007-ops/ha-file-api/total?style=for-the-badge)

<!-- Contributors -->
![Contributors](https://img.shields.io/github/contributors/p3x2007-ops/ha-file-api?style=for-the-badge)

<!-- Last commit -->
![Last commit](https://img.shields.io/github/last-commit/p3x2007-ops/ha-file-api?style=for-the-badge)

<!-- Open issues -->
![Issues](https://img.shields.io/github/issues/p3x2007-ops/ha-file-api?style=for-the-badge)
```

## 📝 Checklist finale

Avant de publier sur les forums :

- [ ] Testez l'installation depuis le repository GitHub
- [ ] Vérifiez que tous les liens fonctionnent
- [ ] Relisez la documentation
- [ ] Préparez réponses aux questions fréquentes :
  - "Est-ce sécurisé ?"
  - "Différence avec File Editor ?"
  - "Comment générer un API secret fort ?"
  - "Compatible avec quelle version de HA ?"

## 🚀 Go live!

Une fois prêt, publiez dans cet ordre :

1. **Home Assistant Forum** (communauté principale)
2. **Reddit** (24h après forum)
3. **Discord** (même jour que Reddit)
4. **Twitter/X** (même jour)
5. **Awesome HA** (PR dans la semaine)
6. **Blog** (dans le mois)

---

**Bonne chance ! 🎉**

Si vous avez des questions, créez une Discussion sur GitHub.
