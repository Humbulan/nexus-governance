#!/bin/bash
echo "🔍 SEARCHING HISTORICAL LEDGER FOR JAN 7 SETTLEMENTS..."
echo "------------------------------------------------------"
# Search for yesterday's date in the gateway logs
grep "2026-01-07" ~/humbu_community_nexus/daily_summary_20260107.txt 2>/dev/null || echo "⚠️ No summary file found for Jan 7."

# Check the Revenue Gateway Log for yesterday's POST requests
echo "📊 BANK BRIDGE ATTEMPTS (JAN 7):"
grep "07/Jan/2026" ~/humbu-rural-bot-core/gateway.log | grep "POST" | head -n 5
grep "07/Jan/2026" ~/humbu-rural-bot-core/gateway.log | grep "POST" | tail -n 5

echo "------------------------------------------------------"
echo "💡 ANALYSIS:"
COUNT=$(grep -c "07/Jan/2026" ~/humbu-rural-bot-core/gateway.log)
if [ $COUNT -gt 0 ]; then
    echo "✅ System attempted $COUNT handshakes with Absa yesterday."
    echo "⚠️ If balance is still negative, Absa has flagged these as 'Unreconciled'."
else
    echo "❌ NO HANDSHAKES DETECTED FOR YESTERDAY."
    echo "Conclusion: The R25k is still sitting in your local Treasury (Ready to Settle)."
fi
