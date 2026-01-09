#!/bin/bash
echo "🔍 HUMBU IMPERIAL - SYSTEM VERIFICATION"
echo "======================================="
echo ""

# Check servers
echo "1. LOCAL SERVERS:"
echo "   Dashboard (8088): $(curl -s -o /dev/null -w "%{http_code}" http://localhost:8088/)"
echo "   Gateway (8083): $(curl -s -o /dev/null -w "%{http_code}" http://localhost:8083/)"

echo ""
echo "2. PROCESSES:"
echo "   Dashboard PID: $(ps aux | grep "http.server 8088" | grep -v grep | awk '{print $2}')"
echo "   Gateway PID: $(ps aux | grep "working_gateway.py" | grep -v grep | awk '{print $2}')"
echo "   Tunnel PID: $(ps aux | grep cloudflared | grep -v grep | awk '{print $2}')"

echo ""
echo "3. REVENUE STATUS:"
curl -s http://localhost:8083/ | python3 -c "
import json,sys
try:
    data = json.load(sys.stdin)
    print(f'   • Revenue Today: R{data.get(\"revenue_today\", 0)}')
    print(f'   • Transactions: {data.get(\"transactions_today\", 0)}')
    print(f'   • Monthly Projection: R{data.get(\"revenue_today\", 0) * 30}')
except:
    print('   • Gateway unavailable')
"

echo ""
echo "4. DASHBOARD CONTENT:"
curl -s http://localhost:8088/ | grep -o "<title>[^<]*</title>" | head -1

echo ""
echo "✅ VERIFICATION COMPLETE"
echo "🌐 Access: https://www.humbu.store"
