#!/bin/bash
# 🏛️ HUMBU IMPERIAL COMMAND SYSTEM

# Function to check revenue
humbu-revenue() {
    local tx_count=$(grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log 2>/dev/null || echo "0")
    local revenue=$(echo "$tx_count * 8.5" | bc 2>/dev/null || echo "0")
    echo "💰 HUMBU IMPERIAL TREASURY"
    echo "=========================="
    echo "Transactions: $tx_count"
    echo "Total Revenue: R$revenue"
    echo "Status: $(if [ "$tx_count" -gt 0 ]; then echo "ACTIVE"; else echo "IDLE"; fi)"
    echo ""
}

# Function to check system status
humbu-status() {
    echo "🛡️ HUMBU IMPERIAL SYSTEM SENTINEL"
    echo "----------------------------------"
    for port in 8088 8089 11434 1808 1880 8086 8087 8082 8083; do
        if (echo > /dev/tcp/127.0.0.1/$port) >/dev/null 2>&1; then
            echo "✅ [$port] Online"
        else
            echo "❌ [$port] Offline"
        fi
    done
    echo "----------------------------------"
}

# Function to show latest receipt
humbu-receipt() {
    local latest_receipt=$(ls -t ~/humbu_community_nexus/shift_receipt_*.json 2>/dev/null | head -1)
    if [ -n "$latest_receipt" ]; then
        echo "📄 LATEST SHIFT RECEIPT"
        echo "======================="
        echo "File: $latest_receipt"
        echo ""
        python3 << 'PYEOF'
import json
import os
import sys

receipt_path = os.path.expanduser("$latest_receipt")
try:
    with open(receipt_path, 'r') as f:
        data = json.load(f)
    
    print(f"Receipt ID: {data.get('receipt_id', 'N/A')}")
    print(f"Shift: {data.get('shift_period', 'N/A')}")
    print(f"Revenue: R{data['financial_summary']['total_revenue']:,.2f}")
    print(f"Transactions: {data['financial_summary']['total_transactions']}")
    print(f"Generated: {data.get('generated_at', 'N/A')[:19]}")
except:
    print("Could not read receipt")
PYEOF
    else
        echo "📭 No receipts found"
        echo "Run: ./generate_shift_receipt.sh"
    fi
}

# Function to show all commands
humbu-help() {
    echo "🏛️ HUMBU IMPERIAL COMMAND SYSTEM"
    echo "================================"
    echo ""
    echo "🎯 CORE COMMANDS:"
    echo "  humbu-ignite              - Start night shift (realistic)"
    echo "  humbu-extinguish          - Graceful shutdown"
    echo "  humbu-status              - System status check"
    echo "  humbu-revenue             - Current revenue"
    echo "  humbu-receipt             - Latest shift receipt"
    echo ""
    echo "📊 MONITORING:"
    echo "  humbu-help                - This help menu"
    echo "  fleet-check               - Fleet status"
    echo ""
    echo "🌐 ACCESS POINTS:"
    echo "  Local Dashboard: http://localhost:8088"
    echo "  Community Portal: http://localhost:8087"
    echo "  Revenue API: http://localhost:8083"
    echo ""
    echo "⏰ REALISTIC SCHEDULE:"
    echo "  20:00 - Start shift"
    echo "  03:16 - Natural flow ends"
    echo "  Auto-receipt generated"
}
