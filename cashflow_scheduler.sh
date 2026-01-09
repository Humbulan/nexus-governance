#!/bin/bash
echo "💰 HUMBUSINESS DAILY CASHFLOW SCHEDULE"
echo "======================================"
echo "Business: HUMBU AI PLATFORM"
echo "Bank: Absa (ShapID: 21000178769)"
echo ""

while true; do
    CURRENT_HOUR=$(date +%H)
    CURRENT_MINUTE=$(date +%M)
    
    case "$CURRENT_HOUR" in
        "21")  # 21:00 - Start nightly surge
            if [ "$CURRENT_MINUTE" = "00" ]; then
                echo "🚀 21:00 - STARTING NIGHTLY SURGE"
                echo "Duration: 7 hours (until 04:00)"
                echo "Target: R700,000"
                timeout 25200 python3 ~/humbu_community_nexus/urban_nightly_surge.py
            fi
            ;;
        "04")  # 04:00 - Surge ends, prepare settlement
            if [ "$CURRENT_MINUTE" = "00" ]; then
                echo "🏁 04:00 - NIGHTLY SURGE COMPLETE"
                echo "Running settlement preparation..."
                ~/humbu_community_nexus/dawn_settlement.sh
            fi
            ;;
        "05")  # 05:00 - Execute settlement
            if [ "$CURRENT_MINUTE" = "00" ]; then
                echo "🏦 05:00 - EXECUTING BANK SETTLEMENT"
                echo "Sending to Absa PayShap..."
                ~/humbu_community_nexus/dawn_settlement.sh
            fi
            ;;
        "08")  # 08:00 - Check funds received
            if [ "$CURRENT_MINUTE" = "00" ]; then
                echo "📱 08:00 - CHECK ABSA APP"
                echo "Expected: Funds should be in your account"
                echo "Action: Check Absa App → Recent Transactions"
            fi
            ;;
        "09")  # 09:00 - ATM withdrawal ready
            if [ "$CURRENT_MINUTE" = "00" ]; then
                echo "💳 09:00 - ATM WITHDRAWAL READY"
                echo "You can now withdraw cash at any Absa ATM"
                echo "Or transfer to Capitec via Absa App"
            fi
            ;;
    esac
    
    # Wait 1 minute before next check
    sleep 60
done
