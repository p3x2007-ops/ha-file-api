# Contributing to File API v2

🇫🇷 **Français** | 🇬🇧 [English](#english)

---

Merci de votre intérêt pour contribuer à File API v2 ! Toute contribution est la bienvenue.

## 🐛 Signaler un bug

1. Vérifiez que le bug n'a pas déjà été signalé dans les [Issues](https://github.com/p3x2007-ops/ha-file-api/issues)
2. Créez une nouvelle issue avec :
   - Description claire du problème
   - Logs de l'add-on (Paramètres → Logs)
   - Version de Home Assistant
   - Configuration utilisée (masquez les secrets)

## ✨ Proposer une fonctionnalité

1. Ouvrez une [Discussion](https://github.com/p3x2007-ops/ha-file-api/discussions) pour en discuter
2. Si approuvée, créez une issue avec :
   - Description détaillée
   - Cas d'usage
   - Exemple de configuration ou d'API

## 🔧 Contribuer du code

1. **Fork** le repository
2. Créez une **branche** : `git checkout -b feature/ma-fonctionnalite`
3. Committez : `git commit -m "Add: ma fonctionnalité"`
4. Poussez : `git push origin feature/ma-fonctionnalite`
5. Ouvrez une **Pull Request**

### Style de code

- Python : PEP 8
- YAML : 2 espaces d'indentation
- Messages de commit en anglais

### Tests

Testez localement avant de soumettre :
```bash
# Build l'image Docker
docker build -t file-api-test file_api_v2/

# Test avec Home Assistant local
```

## 📖 Contribuer à la documentation

La documentation est bilingue (FR/EN). Mettez à jour les deux versions :
- README.md (sections FR et EN)
- QUICKSTART.md + QUICKSTART.en.md
- CONFIGURATION.md + CONFIGURATION.en.md

## 🌍 Traductions

Vous parlez une autre langue ? Aidez-nous à traduire :
1. Créez `README.XX.md` (XX = code langue)
2. Traduisez les fichiers de documentation
3. Soumettez une PR

## 🤝 Code de conduite

- Soyez respectueux et constructif
- Pas de spam ni de contenu offensant
- Acceptez les critiques constructives

---

# English

Thank you for your interest in contributing to File API v2! All contributions are welcome.

## 🐛 Report a bug

1. Check if the bug hasn't already been reported in [Issues](https://github.com/p3x2007-ops/ha-file-api/issues)
2. Create a new issue with:
   - Clear problem description
   - Add-on logs (Settings → Logs)
   - Home Assistant version
   - Configuration used (hide secrets)

## ✨ Propose a feature

1. Open a [Discussion](https://github.com/p3x2007-ops/ha-file-api/discussions) to discuss it
2. If approved, create an issue with:
   - Detailed description
   - Use cases
   - Configuration or API example

## 🔧 Contribute code

1. **Fork** the repository
2. Create a **branch**: `git checkout -b feature/my-feature`
3. Commit: `git commit -m "Add: my feature"`
4. Push: `git push origin feature/my-feature`
5. Open a **Pull Request**

### Code style

- Python: PEP 8
- YAML: 2-space indentation
- Commit messages in English

### Testing

Test locally before submitting:
```bash
# Build Docker image
docker build -t file-api-test file_api_v2/

# Test with local Home Assistant
```

## 📖 Contribute to documentation

Documentation is bilingual (FR/EN). Update both versions:
- README.md (FR and EN sections)
- QUICKSTART.md + QUICKSTART.en.md
- CONFIGURATION.md + CONFIGURATION.en.md

## 🌍 Translations

Do you speak another language? Help us translate:
1. Create `README.XX.md` (XX = language code)
2. Translate documentation files
3. Submit a PR

## 🤝 Code of conduct

- Be respectful and constructive
- No spam or offensive content
- Accept constructive criticism

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.
