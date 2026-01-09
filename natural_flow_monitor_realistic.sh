#!/bin/bash
echo "🌙 REALISTIC NATURAL FLOW MONITOR"
echo "=================================="
echo "Based on actual data: Natural flow ends ~03:16 AM"
echo ""

INITIAL_COUNT=$(grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log)
INITIAL_REVENUE=$(echo "$INITIAL_COUNT * 8.5" | bc)

echo "📊 Starting position:"
echo "• Transactions: $INITIAL_COUNT"
echo "• Revenue: R$INITIAL_REVENUE"
echo ""

echo "⏳ Monitoring natural flow..."
echo "ℹ️ Based on previous pattern, flow may stop around 03:16 AM"
echo ""

LAST_COUNT=$INITIAL_COUNT
STAGNATION_MINUTES=0
MAX_STAGNATION=30  # If no transactions for 30 minutes, harvest is complete

while true; do
    CURRENT_TIME=$(date +%H:%M)
    
    CURRENT_COUNT=$(grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log)
    
    if [ "$CURRENT_COUNT" -eq "$LAST_COUNT" ]; then
        STAGNATION_MINUTES=$((STAGNATION_MINUTES + 1))
        echo "[$CURRENT_TIME] No new transactions (Stagnation: ${STAGNATION_MINUTES}/${MAX_STAGNATION} minutes)"
        
        if [ "$STAGNATION_MINUTES" -ge "$MAX_STAGNATION" ]; then
            echo "🌊 NATURAL FLOW HAS ENDED"
            echo "✅ This is the organic harvest completion"
            break
        fi
    else
        STAGNATION_MINUTES=0
        NEW_TRANSACTIONS=$((CURRENT_COUNT - LAST_COUNT))
        NEW_REVENUE=$(echo "$NEW_TRANSACTIONS * 8.5" | bc)
        TOTAL_REVENUE=$(echo "$CURRENT_COUNT * 8.5" | bc)
        
        echo "[$CURRENT_TIME] +$NEW_TRANSACTIONS tx | +R$NEW_REVENUE | Total: R$TOTAL_REVENUE"
        LAST_COUNT=$CURRENT_COUNT
    fi
    
    sleep 60  # Check every minute
done

# Generate receipt
echo ""
echo "🌾 GENERATING NATURAL HARVEST RECEIPT..."
./generate_shift_receipt.sh

# Sync payout database
echo "🔄 Syncing payout database..."
python3 merchant_payouts_fixed.py --sync-from-log ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log 2>/dev/null || echo "Payout sync optional"

echo ""
echo "✅ NATURAL HARVEST COMPLETE"
echo "   Organic village economics preserved"
echo "   Realistic timing respected"
