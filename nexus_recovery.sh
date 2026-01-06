#!/bin/bash
# 🛡️ HUMBU NEXUS - MASTER RECOVERY & PERSISTENCE
echo "🔄 Initializing Humbu Nexus Recovery..."

# 1. Verify Directory Structure
mkdir -p ~/humbu_community_nexus/logs
mkdir -p ~/humbu_community_nexus/database_backups
mkdir -p ~/humbu_community_nexus/nexus_print_shop

# 2. Check Database Integrity
if [ -f ~/humbu_community_nexus/community_nexus.db ]; then
    echo "✅ Main Database Found."
else
    echo "⚠️ Database missing! Attempting to restore from latest backup..."
    LATEST_BACKUP=$(ls -t ~/humbu_community_nexus/database_backups/*.db 2>/dev/null | head -1)
    if [ -n "$LATEST_BACKUP" ]; then
        cp "$LATEST_BACKUP" ~/humbu_community_nexus/community_nexus.db
        echo "✅ Restored from $LATEST_BACKUP"
    fi
fi

# 3. Restore Permissions
chmod +x ~/humbu_community_nexus/*.sh
chmod +x ~/humbu_community_nexus/*.py

# 4. Restart Background Services
echo "🚀 Restarting Nexus Services..."
pkill -f 'simple_scheduler.py'
pkill -f 'watchdog.py'
nohup python3 ~/humbu_community_nexus/simple_scheduler.py > ~/humbu_community_nexus/logs/scheduler_boot.log 2>&1 &
nohup python3 ~/humbu_community_nexus/watchdog.py > ~/humbu_community_nexus/logs/watchdog_boot.log 2>&1 &

# 5. Final System Pulse
echo "=========================================="
echo "📊 RECOVERY COMPLETE - CURRENT STATS:"
sqlite3 ~/humbu_community_nexus/community_nexus.db "SELECT 'Items: ' || COUNT(*) FROM marketplace;"
echo "Active Crontab Tasks:"
crontab -l | grep -v "^#"
echo "=========================================="
