#!/bin/bash
echo "🛑 HUMBU IMPERIAL - GRACEFUL SHUTDOWN"
echo "======================================"
echo "Timestamp: $(date)"
echo ""

# 1. Stop Revenue Booster
echo "💰 Stopping Revenue Booster..."
pkill -f revenue_booster_fixed.py 2>/dev/null
sleep 1

# 2. Generate final receipt
echo "🧾 Generating final receipt..."
cd ~/humbu_community_nexus
./generate_shift_receipt.sh 2>/dev/null || echo "Receipt generator not found"

# 3. Sync payout database
echo "🔄 Syncing payout database..."
python3 merchant_payouts_fixed.py --sync-from-log ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log 2>/dev/null || echo "Payout sync skipped"

# 4. Stop monitors
echo "🛰️ Stopping monitors..."
pkill -f natural_flow_monitor.sh 2>/dev/null

# 5. Show final revenue
echo ""
echo "📊 FINAL REVENUE REPORT:"
POST_COUNT=$(grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log 2>/dev/null || echo "0")
FINAL_REVENUE=$(echo "$POST_COUNT * 8.5" | bc 2>/dev/null || echo "0")
echo "• Total transactions: $POST_COUNT"
echo "• Total revenue: R$FINAL_REVENUE"

# 6. Keep essential services running
echo ""
echo "✅ ESSENTIAL SERVICES REMAIN:"
echo "• Revenue Gateway (Port 8083) - For manual transactions"
echo "• Community Portal (Port 8087) - For village access"
echo ""
echo "🛡️ SHUTDOWN COMPLETE AT: $(date)"
