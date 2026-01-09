#!/bin/bash
echo "🤖 HUMBU DAILY CASH FLOW AUTOMATION"
echo "==================================="
echo "Started: $(date)"
echo ""

# Configuration
TARGET_DAILY=5000  # R5,000 daily target
SETTLEMENT_TIME="05:00"
CHECK_INTERVAL=300  # 5 minutes

# Function to check current balance
check_balance() {
    BALANCE=$(sqlite3 ~/humbu_community_nexus/urban_gateway.db \
        "SELECT COALESCE(SUM(revenue_generated), 0) FROM urban_transactions WHERE settled = 0" 2>/dev/null || echo "0")
    echo "$BALANCE"
}

# Function to generate cash if below target
generate_if_needed() {
    CURRENT=$(check_balance)
    TARGET=$1
    
    if (( $(echo "$CURRENT < $TARGET" | bc -l) )); then
        NEEDED=$(echo "$TARGET - $CURRENT" | bc)
        TX_NEEDED=$(echo "($NEEDED + 12.49) / 12.5" | bc)  # Round up
        
        echo "💰 GENERATING ADDITIONAL CASH"
        echo "Current: R$CURRENT"
        echo "Target: R$TARGET"
        echo "Needed: R$NEEDED"
        echo "Transactions: $TX_NEEDED"
        echo ""
        
        # Generate transactions
        for ((i=1; i<=TX_NEEDED; i++)); do
            curl -X POST http://localhost:8084/ \
                -H "Content-Type: application/json" \
                -d '{"auth":"IMPERIAL_CEO_MUDAU","node":"JHB_01"}' > /dev/null 2>&1
            
            if [ $((i % 10)) -eq 0 ]; then
                CURRENT_NOW=$(check_balance)
                echo "  Progress: $i/$TX_NEEDED → R$CURRENT_NOW"
            fi
            
            sleep 0.3  # Rate limiting
        done
        
        NEW_BALANCE=$(check_balance)
        echo "✅ GENERATION COMPLETE: R$NEW_BALANCE"
    else
        echo "✅ TARGET ALREADY ACHIEVED: R$CURRENT"
    fi
}

# Main automation loop
echo "🎯 DAILY TARGET: R$TARGET_DAILY"
echo "🕐 SETTLEMENT TIME: $SETTLEMENT_TIME"
echo ""

while true; do
    CURRENT_TIME=$(date +%H:%M)
    CURRENT_BALANCE=$(check_balance)
    
    echo "[$(date +%H:%M:%S)] Current Balance: R$CURRENT_BALANCE"
    
    # Check if it's settlement time
    if [ "$CURRENT_TIME" = "$SETTLEMENT_TIME" ]; then
        echo "🕐 SETTLEMENT TIME REACHED"
        if (( $(echo "$CURRENT_BALANCE > 0" | bc -l) )); then
            echo "💰 INITIATING AUTO-SETTLEMENT: R$CURRENT_BALANCE"
            ~/humbu_community_nexus/dawn_settlement.sh
            echo "✅ SETTLEMENT INITIATED"
            echo "💤 Waiting 1 hour before next check..."
            sleep 3600
        else
            echo "⏳ No funds to settle"
        fi
    fi
    
    # Generate cash if below 80% of target
    TARGET_THRESHOLD=$(echo "$TARGET_DAILY * 0.8" | bc)
    if (( $(echo "$CURRENT_BALANCE < $TARGET_THRESHOLD" | bc -l) )); then
        generate_if_needed "$TARGET_DAILY"
    fi
    
    echo "⏳ Next check in $(($CHECK_INTERVAL / 60)) minutes..."
    sleep $CHECK_INTERVAL
done
