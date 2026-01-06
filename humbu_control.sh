#!/data/data/com.termux/files/usr/bin/bash

clear
echo "🎮 HUMBU COMMUNITY NEXUS - CONTROL PANEL"
echo "========================================"
echo ""

while true; do
    echo "Select option:"
    echo "1. 🚀 Start Platform"
    echo "2. 🛑 Stop Platform"
    echo "3. 📊 Check Status"
    echo "4. 🌐 Open Web Portal"
    echo "5. 🔄 Restart Platform"
    echo "6. 🧹 Clean Terminal"
    echo "7. 📋 Show Commands"
    echo "8. ❌ Exit"
    echo ""
    echo -n "Choice [1-8]: "
    read choice
    
    case $choice in
        1)
            echo "🚀 Starting platform..."
            cd ~/humbu_community_nexus
            pkill -f "community_web.py" 2>/dev/null
            python3 community_web.py &
            echo $! > web_server.pid
            echo "✅ Platform started at http://localhost:8086"
            sleep 2
            ;;
        2)
            echo "🛑 Stopping platform..."
            pkill -f "community_web.py" 2>/dev/null
            echo "✅ Platform stopped"
            sleep 1
            ;;
        3)
            echo "📊 Platform Status:"
            if pgrep -f "community_web.py" >/dev/null; then
                echo "✅ Platform: RUNNING"
                echo "🌐 URL: http://localhost:8086"
                echo ""
                echo "Testing API..."
                curl -s http://localhost:8086/api/stats 2>/dev/null | python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
    print(f'Users: {d[\"stats\"].get(\"total_users\", 0)}')
    print(f'Listings: {d[\"stats\"].get(\"market_listings\", 0)}')
    print(f'Tasks: {d[\"stats\"].get(\"open_tasks\", 0)}')
except:
    print('API not responding yet...')
"
            else
                echo "❌ Platform: STOPPED"
            fi
            ;;
        4)
            echo "🌐 Opening web portal..."
            if command -v termux-open &>/dev/null; then
                termux-open http://localhost:8086
            else
                echo "Visit: http://localhost:8086"
            fi
            ;;
        5)
            echo "🔄 Restarting platform..."
            pkill -f "community_web.py" 2>/dev/null
            sleep 2
            cd ~/humbu_community_nexus
            python3 community_web.py &
            echo $! > web_server.pid
            echo "✅ Platform restarted"
            sleep 2
            ;;
        6)
            clear
            echo "🧹 Terminal cleaned"
            echo "==================="
            ;;
        7)
            echo "📋 Available commands:"
            echo "----------------------"
            echo "cd ~/humbu_community_nexus"
            echo "python3 community_web.py"
            echo "curl http://localhost:8086/api/stats"
            echo "pkill -f 'community_web.py'"
            echo "python3 community_hub.py"
            ;;
        8)
            echo "👋 Exiting..."
            exit 0
            ;;
        *)
            echo "❌ Invalid choice"
            ;;
    esac
    
    echo ""
    echo "Press Enter to continue..."
    read
    clear
    echo "🎮 HUMBU COMMUNITY NEXUS - CONTROL PANEL"
    echo "========================================"
    echo ""
done
