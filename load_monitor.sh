#!/bin/bash
while true; do
    clear
    echo "🌡️ HUMBU NEXUS - SYSTEM LOAD MONITOR"
    echo "===================================="
    echo "Time: $(date)"
    echo ""

    # 1. CPU and RAM usage
    echo "🧠 SYSTEM RESOURCES:"
    top -n 1 -b | head -n 5 | tail -n 2
    echo ""

    # 2. Process Health
    echo "⚙️  ACTIVE SERVICES:"
    if pgrep -f "simple_scheduler.py" > /dev/null; then
        echo "  ✅ Scheduler (PID: $(pgrep -f 'simple_scheduler.py'))"
    else
        echo "  ❌ SCHEDULER DOWN"
    fi

    if pgrep -f "watchdog.py" > /dev/null; then
        echo "  ✅ Watchdog (PID: $(pgrep -f 'watchdog.py'))"
    else
        echo "  ⚠️  Watchdog not running in background"
    fi

    # 3. Database Pressure
    echo ""
    echo "💾 DATABASE PRESSURE:"
    db_size=$(du -h community_nexus.db | cut -f1)
    echo "  Current Size: $db_size"
    
    # 4. Storage Space
    echo "📂 DISK SPACE:"
    df -h . | tail -1 | awk '{print "  Used: " $3 " / Free: " $4}'

    echo ""
    echo "------------------------------------"
    echo "Press Ctrl+C to exit monitor."
    sleep 10
done
