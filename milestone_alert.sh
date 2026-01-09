#!/bin/bash
TARGET=100000
MY_NUMBER="0794658481"

while true; do
    COUNT=$(grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log)
    REVENUE=$(echo "$COUNT * 8.5" | bc)
    
    if (( $(echo "$REVENUE >= $TARGET" | bc -l) )); then
        termux-sms-send -n $MY_NUMBER "💰 MILESTONE! Humbu Imperial has reached R$REVENUE. 54% of monthly target achieved."
        break 
    fi
    sleep 600 
done
