#!/bin/bash
echo "🚀 Launching HMB Imperial Portal..."
cd ~/humbu_community_nexus
echo ""
echo "🏛️ AVAILABLE PAGES:"
echo "1. Navigation Portal: http://localhost:8088/navigation.html"
echo "2. Fleet Command: http://localhost:8088/index.html"
echo "3. Financial Command: http://localhost:8088/financial.html"
echo "4. Village Network: http://localhost:8088/village.html"
echo ""
echo "🌐 PUBLIC ACCESS: humbulan.github.io/nexus-governance/navigation.html"
echo ""
echo "🔄 Starting server if not running..."
pkill -f "python3 -m http.server 8088" 2>/dev/null
python3 -m http.server 8088 > /dev/null 2>&1 &
sleep 2
echo "✅ Imperial Portal Ready!"
