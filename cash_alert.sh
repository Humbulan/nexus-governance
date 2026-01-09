#!/bin/bash
TARGET=5000
while true; do
    # Check the current unsettled balance
    BALANCE=$(sqlite3 ~/humbu_community_nexus/urban_gateway.db "SELECT SUM(revenue_generated) FROM urban_transactions WHERE settled = 0;" 2>/dev/null || echo "0")
    
    # If balance is greater than or equal to target
    if (( $(echo "$BALANCE >= $TARGET" | bc -l) )); then
        echo "💰 TARGET REACHED: R$BALANCE is ready for Absa!"
        # Play a notification sound (Termux system beep or bell)
        echo -e "\a" 
        termux-vibrate -d 1000  # Vibrates for 1 second if Termux:API is installed
        sleep 10
    fi
    sleep 60 # Check every minute
done
