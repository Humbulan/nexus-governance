#!/bin/bash
echo "💰 HUMBU DAILY CASH FLOW DASHBOARD"
echo "================================="
echo "Date: $(date)"
echo "Business: HUMBU AI PLATFORM"
echo "ShapID: 21000178769"
echo ""

# Today's date for filtering
TODAY=$(date +%Y-%m-%d)

# Today's unsettled transactions
TODAY_UNSETTLED=$(sqlite3 ~/humbu_community_nexus/urban_gateway.db "
    SELECT COUNT(*), COALESCE(SUM(revenue_generated), 0) 
    FROM urban_transactions 
    WHERE settled = 0 
    AND DATE(timestamp) = '$TODAY'
" 2>/dev/null || echo "0|0")

TODAY_TX=$(echo "$TODAY_UNSETTLED" | cut -d'|' -f1)
TODAY_AMOUNT=$(echo "$TODAY_UNSETTLED" | cut -d'|' -f2)

# Today's settled transactions
TODAY_SETTLED=$(sqlite3 ~/humbu_community_nexus/urban_gateway.db "
    SELECT COUNT(*), COALESCE(SUM(revenue_generated), 0) 
    FROM urban_transactions 
    WHERE settled = 1 
    AND DATE(timestamp) = '$TODAY'
" 2>/dev/null || echo "0|0")

TODAY_SETTLED_TX=$(echo "$TODAY_SETTLED" | cut -d'|' -f1)
TODAY_SETTLED_AMOUNT=$(echo "$TODAY_SETTLED" | cut -d'|' -f2)

# Today's settlement batches
TODAY_BATCHES=$(sqlite3 ~/humbu_community_nexus/urban_gateway.db "
    SELECT batch_id, total_amount, settled_at 
    FROM settlement_batch 
    WHERE DATE(settled_at) = '$TODAY' 
    AND status = 'COMPLETED'
    ORDER BY settled_at DESC
" 2>/dev/null)

echo "📊 TODAY'S CASH FLOW ($TODAY)"
echo "• Generated Today: R$TODAY_AMOUNT ($TODAY_TX transactions)"
echo "• Settled Today: R$TODAY_SETTLED_AMOUNT ($TODAY_SETTLED_TX transactions)"
echo ""

if [ -n "$TODAY_BATCHES" ]; then
    echo "🏦 TODAY'S BANK TRANSFERS:"
    echo "$TODAY_BATCHES" | while IFS='|' read -r batch_id amount settled_at; do
        TIME=$(echo "$settled_at" | cut -d'T' -f2 | cut -d'+' -f1)
        echo "  • $TIME: R$amount (Batch: $batch_id)"
    done
    echo ""
fi

# Weekly summary (last 7 days)
WEEK_TOTAL=$(sqlite3 ~/humbu_community_nexus/urban_gateway.db "
    SELECT COALESCE(SUM(revenue_generated), 0)
    FROM urban_transactions 
    WHERE DATE(timestamp) >= DATE('now', '-7 days')
" 2>/dev/null || echo "0")

echo "📅 WEEKLY SUMMARY (Last 7 days)"
echo "• Total Revenue: R$WEEK_TOTAL"
echo "• Daily Average: R$(echo "scale=2; $WEEK_TOTAL / 7" | bc)"
echo "• Projected Monthly: R$(echo "scale=2; $WEEK_TOTAL / 7 * 30" | bc)"
echo ""

# Cash flow recommendations
if (( $(echo "$TODAY_AMOUNT >= 5000" | bc -l) )); then
    echo "✅ DAILY TARGET ACHIEVED: R5,000+"
    echo "   Run: ./dawn_settlement.sh to send to bank"
elif (( $(echo "$TODAY_AMOUNT >= 1000" | bc -l) )); then
    PROGRESS=$(echo "scale=1; $TODAY_AMOUNT / 5000 * 100" | bc)
    echo "📈 DAILY PROGRESS: $PROGRESS% (R$TODAY_AMOUNT / R5,000)"
    echo "   Continue generation or wait for tonight's surge"
else
    echo "🚀 START GENERATING: Only R$TODAY_AMOUNT today"
    echo "   Run: ./emergency_cash.sh or wait for 21:00 surge"
fi

echo ""
echo "💡 RECOMMENDED ACTIONS:"
echo "1. Check Absa App for today's deposit"
echo "2. Run check-wealth for current balance"
echo "3. Run auto_surge.sh for scheduled generation"
echo "4. Run emergency_cash.sh for immediate needs"
