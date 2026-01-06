#!/bin/bash
# 🛡️ JSON Health Check - Prevents crashes from malformed JSON

echo "🔍 JSON HEALTH CHECK"
echo "==================="

CHECKED=0
ERRORS=0

# Check all JSON files
find ~/humbu_community_nexus -name "*.json" | while read json_file; do
    CHECKED=$((CHECKED + 1))
    
    if python3 -m json.tool "$json_file" > /dev/null 2>&1; then
        echo "✅ $json_file"
    else
        echo "❌ $json_file - INVALID"
        ERRORS=$((ERRORS + 1))
        
        # Try to fix common issues
        echo "   Attempting repair..."
        
        # Fix missing closing bracket
        if ! tail -1 "$json_file" | grep -q ']'; then
            echo "]" >> "$json_file"
            echo "   Added missing closing bracket"
        fi
        
        # Fix missing comma between objects
        sed -i ':a;N;$!ba;s/}\n{/},\n{/g' "$json_file"
        
        # Re-check
        if python3 -m json.tool "$json_file" > /dev/null 2>&1; then
            echo "   ✅ Repair successful"
            ERRORS=$((ERRORS - 1))
        else
            echo "   ❌ Repair failed - manual fix needed"
        fi
    fi
done

echo ""
echo "📊 SUMMARY:"
echo "   Files checked: $CHECKED"
echo "   Errors found: $ERRORS"

if [ $ERRORS -eq 0 ]; then
    echo "✅ All JSON files are valid"
else
    echo "⚠️  $ERRORS files need attention"
    echo "   Run: python3 -m json.tool [file] to see specific error"
fi
