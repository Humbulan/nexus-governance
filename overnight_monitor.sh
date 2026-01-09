#!/bin/bash
echo "🌙 OVERNIGHT REVENUE MONITOR"
echo "============================="
echo "Starting at: $(date)"
echo "Target end: 06:00 AM tomorrow"
echo ""

INITIAL_COUNT=$(grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log)
echo "Initial transaction count: $INITIAL_COUNT"
echo "Initial revenue: R$(echo "$INITIAL_COUNT * 8.5" | bc)"
echo ""

while true; do
    CURRENT_TIME=$(date +%H:%M)
    if [ "$CURRENT_TIME" = "06:00" ]; then
        echo "⏰ 06:00 AM REACHED - FINAL REPORT"
        break
    fi
    
    CURRENT_COUNT=$(grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log)
    NEW_TRANSACTIONS=$((CURRENT_COUNT - INITIAL_COUNT))
    NEW_REVENUE=$(echo "$NEW_TRANSACTIONS * 8.5" | bc)
    
    echo "[$CURRENT_TIME] New: +$NEW_TRANSACTIONS tx | +R$NEW_REVENUE | Total: R$(echo "$CURRENT_COUNT * 8.5" | bc)"
    
    sleep 300  # Check every 5 minutes
done

FINAL_COUNT=$(grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log)
FINAL_REVENUE=$(echo "$FINAL_COUNT * 8.5" | bc)
OVERNIGHT_TRANSACTIONS=$((FINAL_COUNT - INITIAL_COUNT))
OVERNIGHT_REVENUE=$(echo "$OVERNIGHT_TRANSACTIONS * 8.5" | bc)

echo ""
echo "🏁 OVERNIGHT RESULTS:"
echo "====================="
echo "• Total transactions: $FINAL_COUNT"
echo "• Total revenue: R$FINAL_REVENUE"
echo "• Overnight transactions: $OVERNIGHT_TRANSACTIONS"
echo "• Overnight revenue: R$OVERNIGHT_REVENUE"
echo "• Average rate: R$(echo "scale=2; $OVERNIGHT_REVENUE / 8" | bc)/hour"
echo "✅ Mission accomplished!"
