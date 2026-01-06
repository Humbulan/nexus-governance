#!/bin/bash

echo "🔧 Humbu Community Nexus - Backup Manager"
echo "========================================"

case "$1" in
    start)
        ./start_scheduler.sh
        ;;
    stop)
        pkill -f "python3 termux_scheduler.py" 2>/dev/null
        if [ $? -eq 0 ]; then
            echo "✅ Scheduler stopped"
        else
            echo "ℹ️  No scheduler running"
        fi
        ;;
    status)
        if pgrep -f "python3 termux_scheduler.py" > /dev/null; then
            echo "✅ Scheduler is RUNNING"
            echo "📊 Last log entries:"
            tail -5 scheduler.log 2>/dev/null || echo "No log file found"
        else
            echo "❌ Scheduler is STOPPED"
        fi
        
        echo ""
        echo "📁 Backup Status:"
        echo "  Monthly backups: $(ls -1 database_backups/*.db 2>/dev/null | wc -l) files"
        echo "  Weekly backups: $(find weekly_backups -name "*.db" 2>/dev/null | wc -l) files"
        echo "  Log files: $(ls -1 logs/*.log 2>/dev/null | wc -l) files"
        ;;
    backup-now)
        echo "🔄 Creating manual backup..."
        python3 weekly_backup.py
        ;;
    check-backups)
        echo "🔍 Checking backup integrity..."
        latest=$(ls -t database_backups/*.db 2>/dev/null | head -1)
        if [ -f "$latest" ]; then
            echo "Latest backup: $latest"
            sqlite3 "$latest" "PRAGMA integrity_check;" 2>/dev/null
            if [ $? -eq 0 ]; then
                echo "✅ Backup integrity: PASS"
            else
                echo "❌ Backup integrity: FAIL"
            fi
        else
            echo "No backups found"
        fi
        ;;
    logs)
        echo "📋 Recent logs:"
        tail -20 scheduler.log 2>/dev/null || echo "No log file found"
        ;;
    *)
        echo "Usage: $0 {start|stop|status|backup-now|check-backups|logs}"
        echo ""
        echo "Commands:"
        echo "  start         - Start the backup scheduler"
        echo "  stop          - Stop the backup scheduler"
        echo "  status        - Check scheduler and backup status"
        echo "  backup-now    - Create a manual backup immediately"
        echo "  check-backups - Verify backup integrity"
        echo "  logs          - View recent logs"
        exit 1
        ;;
esac
