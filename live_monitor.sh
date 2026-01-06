#!/bin/bash
echo "📡 LIVE REVENUE MONITOR"
echo "======================="
echo "Press Ctrl+C to stop"
echo ""

PREV_TOTAL=14064
while true; do
    clear
    echo "📡 LIVE REVENUE MONITOR - $(date '+%H:%M:%S')"
    echo "=========================================="
    
    # Get current status
    STATUS=$(curl -s http://localhost:8083/ 2>/dev/null)
    
    if [ -n "$STATUS" ]; then
        CURRENT_TOTAL=$(echo "$STATUS" | python3 -c "
import json, sys
data = json.load(sys.stdin)
print(data.get('revenue_today', 0))
")
        
        CURRENT_TX=$(echo "$STATUS" | python3 -c "
import json, sys
data = json.load(sys.stdin)
print(data.get('transactions_today', 0))
")
        
        # Calculate changes
        REV_CHANGE=$((CURRENT_TOTAL - PREV_TOTAL))
        PREV_TOTAL=$CURRENT_TOTAL
        
        # Display
        echo "💰 TODAY'S REVENUE: R$CURRENT_TOTAL"
        echo "📊 TRANSACTIONS: $CURRENT_TX"
        echo "📈 LAST MINUTE: +R$REV_CHANGE"
        echo ""
        echo "🎯 TARGET PROGRESS (R1M/month):"
        MONTHLY=$((CURRENT_TOTAL * 30))
        PROGRESS=$(echo "scale=1; ($MONTHLY / 1000000) * 100" | bc)
        echo "• Current: R$MONTHLY/month"
        echo "• Progress: ${PROGRESS}%"
        echo ""
        
        # Progress bar
        BAR_WIDTH=50
        FILL=$(echo "scale=0; $PROGRESS * $BAR_WIDTH / 100" | bc)
        BAR="["
        for ((i=0; i<BAR_WIDTH; i++)); do
            if [ $i -lt $FILL ]; then
                BAR="${BAR}█"
            else
                BAR="${BAR}░"
            fi
        done
        BAR="${BAR}]"
        echo "$BAR"
        
        # Check stress test
        if pgrep -f heavy_load_test.sh > /dev/null; then
            echo ""
            echo "⚡ STRESS TEST: ACTIVE"
        fi
    else
        echo "❌ Gateway offline"
    fi
    
    sleep 5
done
