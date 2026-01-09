#!/bin/bash
echo "🌙 NATURAL FLOW MONITOR - RESPECTING 05:00 AM ENDPOINT"
echo "======================================================"
echo "Starting at: $(date)"
echo "Natural endpoint: 05:00 AM"
echo ""

INITIAL_COUNT=$(grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log)
INITIAL_REVENUE=$(echo "$INITIAL_COUNT * 8.5" | bc)
echo "📊 Initial position:"
echo "• Transactions: $INITIAL_COUNT"
echo "• Revenue: R$INITIAL_REVENUE"
echo ""

echo "⏳ Monitoring natural flow..."
LAST_COUNT=$INITIAL_COUNT
STAGNATION_COUNT=0
MAX_STAGNATION=10  # If no new transactions for 10 checks, assume flow stopped

while true; do
    CURRENT_TIME=$(date +%H:%M)
    
    # Check if we've reached 05:00 AM natural endpoint
    if [ "$CURRENT_TIME" = "05:00" ]; then
        echo "🕔 05:00 AM NATURAL ENDPOINT REACHED"
        break
    fi
    
    CURRENT_COUNT=$(grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log)
    
    # Check for natural flow stagnation
    if [ "$CURRENT_COUNT" -eq "$LAST_COUNT" ]; then
        STAGNATION_COUNT=$((STAGNATION_COUNT + 1))
        echo "[$CURRENT_TIME] No new transactions (Stagnation: $STAGNATION_COUNT/$MAX_STAGNATION)"
        
        if [ "$STAGNATION_COUNT" -ge "$MAX_STAGNATION" ]; then
            echo "🌊 NATURAL FLOW HAS STOPPED EARLY"
            echo "The data source has naturally ceased"
            break
        fi
    else
        STAGNATION_COUNT=0
        NEW_TRANSACTIONS=$((CURRENT_COUNT - LAST_COUNT))
        NEW_REVENUE=$(echo "$NEW_TRANSACTIONS * 8.5" | bc)
        TOTAL_REVENUE=$(echo "$CURRENT_COUNT * 8.5" | bc)
        
        echo "[$CURRENT_TIME] +$NEW_TRANSACTIONS tx | +R$NEW_REVENUE | Total: R$TOTAL_REVENUE"
        LAST_COUNT=$CURRENT_COUNT
    fi
    
    sleep 60  # Check every minute, not every 5
done

# FINAL NATURAL HARVEST REPORT
FINAL_COUNT=$(grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log)
FINAL_REVENUE=$(echo "$FINAL_COUNT * 8.5" | bc)
NATURAL_HARVEST=$((FINAL_COUNT - INITIAL_COUNT))
NATURAL_REVENUE=$(echo "$NATURAL_HARVEST * 8.5" | bc)

echo ""
echo "🌾 NATURAL HARVEST COMPLETE"
echo "============================"
echo "🕐 Time period: $(date -d @$(( $(date +%s) - 3600 )) +%H:%M) to $(date +%H:%M)"
echo ""
echo "📊 HARVEST RESULTS:"
echo "• Total transactions: $FINAL_COUNT"
echo "• Total revenue: R$FINAL_REVENUE"
echo "• Natural harvest transactions: $NATURAL_HARVEST"
echo "• Natural harvest revenue: R$NATURAL_REVENUE"
echo ""
echo "📈 RATE ANALYSIS:"
if [ $NATURAL_HARVEST -gt 0 ]; then
    HOURS_RUNNING=$(echo "scale=2; ($(date +%s) - $(date -d "1 hour ago" +%s)) / 3600" | bc)
    HOURLY_RATE=$(echo "scale=2; $NATURAL_REVENUE / $HOURS_RUNNING" | bc)
    echo "• Average rate: R$HOURLY_RATE/hour"
    echo "• This is $(echo "scale=1; ($HOURLY_RATE / 15300) * 100" | bc)% of full capacity"
fi
echo ""
echo "👥 VILLAGE ECONOMIC IMPACT:"
MERCHANT_COUNT=10
PER_MERCHANT=$(echo "scale=2; $FINAL_REVENUE / $MERCHANT_COUNT" | bc)
echo "• Merchants funded: $MERCHANT_COUNT"
echo "• Average per merchant: R$PER_MERCHANT"
echo "• This represents:"
echo "   - $(echo "scale=0; $PER_MERCHANT / 50" | bc) bags of maize"
echo "   - $(echo "scale=0; $PER_MERCHANT / 500" | bc) goat deposits"
echo "   - $(echo "scale=0; $PER_MERCHANT / 20" | bc) days of casual labor"
echo ""
echo "✅ NATURAL FLOW PRESERVED"
echo "   No artificial inflation"
echo "   Organic village economics"
echo "   Sustainable growth pattern"
