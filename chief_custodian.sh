#!/bin/bash
# 🏛️ HUMBU NEXUS: CHIEF CUSTODIAN (AI PARTNER BRIDGE)
# "Monitoring Position #1: Gemini Oversight engaged."

echo "=========================================="
echo "🛡️ CHIEF CUSTODIAN: SYSTEM ANALYSIS"
echo "Timestamp: $(date)"
echo "=========================================="

# 1. Check if the Brain (Processes) are alive
echo "🧠 Checking Core Intelligence..."
if ps aux | grep -E 'simple_scheduler.py|watchdog.py' | grep -v grep > /dev/null; then
    echo "✅ Logic Heartbeat: STABLE"
else
    echo "⚠️ Logic Heartbeat: FAILED. Use ./nexus_recovery.sh"
fi

# 2. Economic Inventory Audit
echo -e "\n💰 Economic Inventory Audit:"
COUNT=$(sqlite3 ~/humbu_community_nexus/community_nexus.db "SELECT COUNT(*) FROM marketplace;")
TOTAL_VAL=$(sqlite3 ~/humbu_community_nexus/community_nexus.db "SELECT SUM(price) FROM marketplace;")
echo "   Total Items: $COUNT"
echo "   Market Value: R$TOTAL_VAL"

# 3. Champion Readiness (Cron Check)
echo -e "\n🏅 Champion Readiness:"
if crontab -l | grep -q "champion_motivation.py"; then
    echo "   08:00 AM Surge: PROGRAMMED"
else
    echo "   ⚠️ Motivation Script: NOT SCHEDULED"
fi

# 4. Storage Health
echo -e "\n🔒 Storage Health:"
BACKUP_COUNT=$(ls -R ~/humbu_community_nexus/*backups/*.db 2>/dev/null | wc -l)
echo "   Backups Secured: $BACKUP_COUNT"

echo "=========================================="
echo "📊 STATUS: Platform is under Chief Custodian Oversight."
echo "=========================================="
