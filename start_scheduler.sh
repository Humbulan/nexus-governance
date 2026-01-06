#!/bin/bash

echo "🚀 Starting Humbu Community Nexus Scheduler..."
echo "Date: $(date)"
echo ""

# Change to project directory
cd /data/data/com.termux/files/home/humbu_community_nexus

# Create necessary directories
mkdir -p logs
mkdir -p database_backups
mkdir -p weekly_backups

# Kill any existing scheduler
pkill -f "python3 simple_scheduler.py" 2>/dev/null
pkill -f "python3 termux_scheduler.py" 2>/dev/null

# Start the new scheduler
nohup python3 simple_scheduler.py > scheduler_output.log 2>&1 &

# Wait for it to start
sleep 3

# Check if it's running
if pgrep -f "python3 simple_scheduler.py" > /dev/null; then
    echo "✅ Scheduler started successfully!"
    echo ""
    echo "📊 Scheduler Information:"
    echo "  PID: $(pgrep -f 'python3 simple_scheduler.py')"
    echo "  Log file: scheduler.log"
    echo "  Output log: scheduler_output.log"
    echo ""
    echo "📅 Scheduled Jobs:"
    echo "  • Weekly Backup: Sunday 00:00"
    echo "  • Daily Backup: Every day 02:00"
    echo "  • Daily Status: Every day 08:00"
    echo "  • Monthly Maintenance: 1st of month 03:00"
    echo ""
    echo "🔧 Management Commands:"
    echo "  Check status: ./manage_backups.sh status"
    echo "  Stop scheduler: ./manage_backups.sh stop"
    echo "  View logs: tail -f scheduler.log"
    echo ""
    echo "📋 Recent logs:"
    tail -5 scheduler.log 2>/dev/null || echo "  No logs yet - check back in a minute"
else
    echo "❌ Failed to start scheduler"
    echo ""
    echo "📝 Checking error logs..."
    tail -20 scheduler_output.log 2>/dev/null || echo "  No output log found"
    echo ""
    echo "🔧 Troubleshooting steps:"
    echo "  1. Check if Python is installed: python3 --version"
    echo "  2. Check if schedule module is installed: pip list | grep schedule"
    echo "  3. Check disk space: df -h ."
fi
