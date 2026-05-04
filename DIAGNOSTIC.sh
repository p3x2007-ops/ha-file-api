#!/bin/bash

echo "════════════════════════════════════════════════════════════"
echo "  🔍 DIAGNOSTIC COMPLET DU REPOSITORY ADD-ON"
echo "════════════════════════════════════════════════════════════"
echo ""

cd /Users/iMac/claude-files/ha-file-api

echo "📁 STRUCTURE DU REPOSITORY :"
echo "----------------------------"
tree -L 2 -a --charset ascii 2>/dev/null || find . -maxdepth 2 -not -path "./.git/*" -not -path "./.claude/*" | sort
echo ""

echo "✅ FICHIERS OBLIGATOIRES :"
echo "--------------------------"
if [ -f "repository.yaml" ]; then
    echo "✓ repository.yaml présent"
    cat repository.yaml
else
    echo "✗ repository.yaml MANQUANT !"
fi
echo ""

if [ -d "file-api" ]; then
    echo "✓ Dossier file-api/ présent"

    echo ""
    echo "📄 CONFIG.YAML :"
    echo "----------------"
    if [ -f "file-api/config.yaml" ]; then
        echo "✓ config.yaml présent"
        echo ""
        echo "Champs clés :"
        grep -E "^(name|version|slug|description):" file-api/config.yaml
        echo ""

        # Vérifier cohérence slug / nom dossier
        SLUG=$(grep "^slug:" file-api/config.yaml | awk '{print $2}' | tr -d '"')
        if [ "$SLUG" = "file-api" ]; then
            echo "✓ slug '$SLUG' correspond au nom du dossier"
        else
            echo "✗ ERREUR : slug '$SLUG' ne correspond PAS au dossier 'file-api'"
        fi
    else
        echo "✗ config.yaml MANQUANT !"
    fi

    echo ""
    echo "🖼️  ICÔNES :"
    echo "-----------"
    if [ -f "file-api/icon.png" ]; then
        SIZE=$(sips -g pixelWidth -g pixelHeight file-api/icon.png 2>/dev/null | grep pixel | awk '{print $2}' | tr '\n' 'x' | sed 's/x$//')
        echo "✓ icon.png présent ($SIZE)"
    else
        echo "✗ icon.png MANQUANT !"
    fi

    if [ -f "file-api/logo.png" ]; then
        SIZE=$(sips -g pixelWidth -g pixelHeight file-api/logo.png 2>/dev/null | grep pixel | awk '{print $2}' | tr '\n' 'x' | sed 's/x$//')
        echo "✓ logo.png présent ($SIZE)"
    else
        echo "○ logo.png absent (optionnel)"
    fi

    echo ""
    echo "🐳 BUILD FILES :"
    echo "----------------"
    [ -f "file-api/Dockerfile" ] && echo "✓ Dockerfile" || echo "✗ Dockerfile MANQUANT"
    [ -f "file-api/build.yaml" ] && echo "✓ build.yaml" || echo "○ build.yaml absent (optionnel)"
    [ -f "file-api/README.md" ] && echo "✓ README.md" || echo "○ README.md absent (optionnel)"

else
    echo "✗ Dossier file-api/ MANQUANT !"
fi

echo ""
echo "🌐 VÉRIFICATION GITHUB :"
echo "------------------------"
if gh auth status &> /dev/null; then
    echo "✓ GitHub CLI authentifié"

    echo ""
    echo "Fichiers sur GitHub (branche main) :"
    gh api repos/p3x2007-ops/ha-file-api/contents --jq '.[].name' | sort

    echo ""
    echo "Derniers commits :"
    git log --oneline -3
else
    echo "○ GitHub CLI non disponible"
fi

echo ""
echo "════════════════════════════════════════════════════════════"
echo "  📋 CHECKLIST FINALE"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "Pour que l'add-on apparaisse dans Home Assistant :"
echo ""
echo "  1. ✓ repository.yaml à la racine"
echo "  2. ✓ file-api/config.yaml avec slug correct"
echo "  3. ✓ file-api/icon.png (128x128 min)"
echo "  4. ✓ file-api/Dockerfile"
echo "  5. ✓ Poussé sur GitHub"
echo ""
echo "Dans Home Assistant :"
echo "  → Supprimer le repository"
echo "  → Ajouter : https://github.com/p3x2007-ops/ha-file-api"
echo "  → Attendre 30 secondes"
echo "  → Vérifier la boutique"
echo ""
echo "Si toujours rien, vérifier les logs du Supervisor :"
echo "  → Paramètres → Système → Journaux"
echo "  → Sélectionner 'Supervisor'"
echo "  → Rechercher des erreurs liées au repository"
echo ""
echo "════════════════════════════════════════════════════════════"
