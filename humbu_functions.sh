#!/bin/bash
# 🏛️ CLEAN HUMBU FUNCTIONS - NO ALIAS OVERRIDES

humbu-revenue-clean() {
    local tx_count
    local revenue
    
    # Safely get transaction count
    if [ -f ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log ]; then
        tx_count=$(grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log 2>/dev/null || echo "0")
    else
        tx_count="0"
    fi
    
    # Calculate revenue
    revenue=$(echo "$tx_count * 8.5" | bc 2>/dev/null || echo "0")
    
    echo "💰 HUMBU IMPERIAL TREASURY"
    echo "=========================="
    echo "Transactions: $tx_count"
    echo "Total Revenue: R$revenue"
    echo ""
}

humbu-receipt-clean() {
    local latest_receipt=$(ls -t ~/humbu_community_nexus/shift_receipt_*.json 2>/dev/null | head -1)
    if [ -n "$latest_receipt" ] && [ -f "$latest_receipt" ]; then
        echo "📄 LATEST SHIFT RECEIPT"
        echo "======================="
        echo "File: $(basename "$latest_receipt")"
        echo "Path: $latest_receipt"
        echo ""
        echo "To view: cat $latest_receipt | python3 -m json.tool"
    else
        echo "📭 No receipts found"
    fi
}

# Simple one-liners
alias hr='humbu-revenue-clean'
alias hrc='humbu-receipt-clean'
