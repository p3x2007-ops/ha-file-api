#!/bin/bash

echo "════════════════════════════════════════════════════════"
echo "  🚀 SCRIPT DE PUSH VERS GITHUB"
echo "════════════════════════════════════════════════════════"
echo ""

cd /Users/iMac/claude-files/ha-file-api

echo "📍 Dossier actuel : $(pwd)"
echo ""

# Vérifier si gh est authentifié
if gh auth status &> /dev/null; then
    echo "✅ GitHub CLI déjà authentifié"
    echo ""
    echo "📤 Création et push du repository..."
    echo ""
    
    # Créer et pousser
    gh repo create p3x2007-ops/ha-file-api --public --source=. --remote=origin --push
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "════════════════════════════════════════════════════════"
        echo "  ✅ SUCCÈS ! Repository créé et poussé !"
        echo "════════════════════════════════════════════════════════"
        echo ""
        echo "🔗 Voir sur GitHub :"
        echo "   https://github.com/p3x2007-ops/ha-file-api"
        echo ""
        echo "🏠 Dans Home Assistant :"
        echo "   1. Paramètres → Modules → Boutique → ⋮ → Repositories"
        echo "   2. Ajouter : https://github.com/p3x2007-ops/ha-file-api"
        echo "   3. Rafraîchir → Installer 'File API v2'"
        echo ""
    else
        echo ""
        echo "❌ Erreur lors de la création du repository"
        echo "Le repo existe peut-être déjà ? Essayez :"
        echo "   git push -u origin main --force"
        echo ""
    fi
else
    echo "🔑 GitHub CLI pas authentifié"
    echo ""
    echo "➡️  Étape 1 : Authentifier GitHub CLI"
    echo ""
    echo "   Exécutez : gh auth login"
    echo ""
    echo "   Puis choisissez :"
    echo "   - GitHub.com"
    echo "   - HTTPS"
    echo "   - Authentifier via navigateur"
    echo ""
    echo "➡️  Étape 2 : Re-exécuter ce script"
    echo ""
    echo "   bash PUSH_MAINTENANT.sh"
    echo ""
fi

echo "════════════════════════════════════════════════════════"
