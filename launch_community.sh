#!/data/data/com.termux/files/usr/bin/bash

echo "🚀 LAUNCHING HUMBU COMMUNITY NEXUS"
echo "🌍 People's Economic Platform"
echo "================================"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

cd ~/humbu_community_nexus

echo -e "${BLUE}📊 Step 1: Initializing Community Database...${NC}"
python3 community_hub.py

echo -e "\n${BLUE}🌐 Step 2: Starting Web Portal...${NC}"
echo -e "${YELLOW}Web portal will run on: http://localhost:8086${NC}"
echo -e "${YELLOW}Press Ctrl+C to stop the server${NC}"
echo -e "${GREEN}✅ Open browser and visit: http://localhost:8086${NC}"

# Start web server in background
python3 community_web.py &

# Save PID
WEB_PID=$!
echo $WEB_PID > web_server.pid

echo -e "\n${BLUE}📱 Step 3: Community Platform Ready!${NC}"
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}🌐 WEB PORTAL: http://localhost:8086${NC}"
echo -e "${GREEN}📊 API ENDPOINTS:${NC}"
echo -e "  • /api/stats      - Community statistics"
echo -e "  • /api/marketplace - Marketplace listings"
echo -e "  • /api/tasks      - Available tasks"
echo -e "  • /api/map        - Map data (JSON)"
echo -e "${GREEN}📁 DATA FILES:${NC}"
echo -e "  • ~/humbu_community_nexus/community_map.json"
echo -e "  • ~/humbu_community_nexus/data/community.db"
echo -e "${GREEN}🚀 BUSINESS MODEL:${NC}"
echo -e "  • Marketplace: 2% transaction fee"
echo -e "  • Task Platform: 5% service fee"
echo -e "  • Wallet System: R50 welcome bonus"
echo -e "${GREEN}🌍 TARGET VILLAGES:${NC}"
echo -e "  • Thohoyandou, Sibasa, Manini, Mukhomi"
echo -e "  • Malamulele, Gundo, Makhuvha, Folovhodwe"

echo -e "\n${YELLOW}🎯 NEXT STEPS:${NC}"
echo -e "1. Register first 100 community members"
echo -e "2. Connect to mobile money APIs"
echo -e "3. Launch USSD interface (*134*600#)"
echo -e "4. Deploy to physical villages"

echo -e "\n${BLUE}🛑 To stop the platform:${NC}"
echo -e "kill \$(cat web_server.pid) 2>/dev/null; echo 'Platform stopped'"

# Keep script running
wait $WEB_PID
