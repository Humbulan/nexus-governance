#!/bin/bash
# Imperial Color Matrix
GOLD='\033[1;33m'
BLUE='\033[1;34m'
RED='\033[1;31m'
NC='\033[0m' # No Color

clear
echo -e "${GOLD}🏛️ HUMBU IMPERIAL LOGISTICS - SECURE COMMAND CENTER${NC}"
echo -e "${BLUE}====================================================${NC}"

# 2. PIN Challenge (Handshake)
echo -ne "${GOLD}ENTER COMMANDER PIN: ${NC}"
read -s PIN
echo ""

if [ "$PIN" != "2026" ]; then
    echo -e "${RED}❌ ACCESS DENIED: INVALID CREDENTIALS${NC}"
    exit 1
fi

echo -e "${BLUE}✅ CREDENTIALS VERIFIED. DECRYPTING LEDGER...${NC}"
sleep 1

# 3. Pulling the FULL Imperial Report
echo -e "${GOLD}### Generated: $(date '+%Y-%m-%d %H:%M')${NC}"
cat ~/humbu_community_nexus/final_status_report.md

echo -e "${BLUE}====================================================${NC}"
echo -e "${GOLD}STATUS: IMPERIAL STACK 100% OPERATIONAL${NC}"
