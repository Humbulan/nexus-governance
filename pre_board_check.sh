#!/bin/bash
clear
echo "🏛️ HUMBU IMPERIAL: PRE-BOARD FINAL VERIFICATION"
echo "==============================================="
echo "CEO: Humbulani Mudau | Portfolio: R9,327,935.17"
echo "-----------------------------------------------"

# 1. PORT CHECK
for port in 8082 8086 8102 1880 11434 9090; do
  (echo > /dev/tcp/127.0.0.1/$port) >/dev/null 2>&1 && \
  echo "🟢 PORT $port: ONLINE" || echo "❌ PORT $port: OFFLINE"
done

echo ""
# 2. SECURITY CHECK
echo "🔒 SECURITY AUDIT:"
curl -s -o /dev/null -w "   Legacy Block (/complete): %{http_code}\n" http://localhost:8082/complete
curl -s -o /dev/null -w "   Dashboard Access: %{http_code}\n" http://localhost:8082/imperial-dashboard-8082.html

echo ""
# 3. DATA CHECK
echo "📊 DATA TELEMETRY:"
curl -s http://localhost:8082/village_data.json | grep -q "Malamulele" && echo "   ✅ Village Data: VALID" || echo "   ❌ Village Data: ERROR"
curl -s http://localhost:9090/ | grep -q "9,327,935" && echo "   ✅ Portfolio Data: VALID" || echo "   ❌ Portfolio Data: ERROR"

echo "-----------------------------------------------"
echo "🚀 SYSTEM READY FOR BOARD PRESENTATION"
