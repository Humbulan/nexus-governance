#!/bin/bash
echo "🏦 ABSA ACCOUNT STATUS CHECK"
echo "============================"
echo "Business: HUMBU AI PLATFORM"
echo "Account: 4121505543"
echo "ShapID: 21000178769"
echo ""

# Get last settlement details
LAST_SETTLEMENT=$(sqlite3 ~/humbu_community_nexus/urban_gateway.db "
    SELECT batch_id, total_amount, settled_at 
    FROM settlement_batch 
    WHERE status = 'COMPLETED' 
    ORDER BY settled_at DESC 
    LIMIT 1
" 2>/dev/null)

if [ -n "$LAST_SETTLEMENT" ]; then
    BATCH_ID=$(echo "$LAST_SETTLEMENT" | cut -d'|' -f1)
    AMOUNT=$(echo "$LAST_SETTLEMENT" | cut -d'|' -f2)
    SETTLED_AT=$(echo "$LAST_SETTLEMENT" | cut -d'|' -f3)
    TIME_AGO=$(python3 -c "
from datetime import datetime, timezone
import sys
settled = '$SETTLED_AT'
if '+' in settled:
    settled = settled.split('+')[0]
dt = datetime.fromisoformat(settled.replace('Z', '+00:00'))
now = datetime.now(timezone.utc)
diff = now - dt.replace(tzinfo=timezone.utc)
hours = diff.total_seconds() / 3600
print(f'{hours:.1f}')
")
    
    echo "📅 LAST SETTLEMENT:"
    echo "• Amount: R$AMOUNT"
    echo "• Time: $SETTLED_AT"
    echo "• Hours ago: $TIME_AGO"
    echo ""
    
    if (( $(echo "$TIME_AGO < 2" | bc -l) )); then
        echo "⏳ STATUS: FUNDS IN TRANSIT"
        echo "   Expected in Absa App: Within 1-2 hours"
        echo "   Check your Absa App now"
    elif (( $(echo "$TIME_AGO < 24" | bc -l) )); then
        echo "✅ STATUS: FUNDS SHOULD BE AVAILABLE"
        echo "   Check Absa App → Recent Transactions"
        echo "   Withdraw at any Absa ATM"
    else
        echo "ℹ️ STATUS: SETTLED MORE THAN 24 HOURS AGO"
        echo "   Check Absa App for historical deposits"
    fi
else
    echo "❌ NO RECENT SETTLEMENTS FOUND"
    echo "   Run: ./dawn_settlement.sh to send funds to Absa"
fi

echo ""
echo "💳 ABSA APP CHECKLIST:"
echo "1. Open Absa Banking App"
echo "2. Go to 'Recent Transactions'"
echo "3. Look for deposit from HUMBU AI PLATFORM"
echo "4. Check available balance"
echo "5. Note: May show as 'PayShap Transfer'"
echo ""
echo "🏧 ATM WITHDRAWAL:"
echo "• Use your Absa card at any Absa ATM"
echo "• Maximum daily withdrawal: Usually R5,000"
echo "• Fees: Check Absa fee structure"
echo ""
echo "🔄 CAPITEC TRANSFER:"
echo "• In Absa App: Payments → Rapid Transfer"
echo "• Enter Capitec phone number linked to account"
echo "• Instant transfer available"
