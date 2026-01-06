#!/bin/bash
clear
echo "🏛️ HUMBU IMPERIAL CONTROL PANEL"
echo "================================"
echo "IDC: #4000120009 | Sage: R9M Forecast"
echo "Dashboard: monitor.humbu.store"
echo ""

while true; do
    echo "1. 🚀 Start Community Portal (Auto-port)"
    echo "2. 🛑 Stop All Services"
    echo "3. 📊 Check Imperial Status"
    echo "4. 🌐 Open Executive Dashboard"
    echo "5. 🔄 Run Revival Protocol"
    echo "6. 🧠 Generate Sage Intelligence"
    echo "7. 🌍 Test Public Access"
    echo "8. 📧 IDC Briefing Package"
    echo "9. ❌ Exit"
    echo ""
    read -p "Choice [1-9]: " choice
    
    case $choice in
        1)
            echo "🔍 Finding available port..."
            for port in {8086..8090}; do
                if ! nc -z localhost $port 2>/dev/null; then
                    echo "🚀 Launching Community Portal on port $port"
                    cd ~/humbu_community_nexus
                    nohup python3 community_web_fixed.py --port $port > ~/logs/community_$port.log 2>&1 &
                    sleep 3
                    if nc -z localhost $port 2>/dev/null; then
                        echo "✅ Success! Access: http://localhost:$port"
                        echo "📡 Serving: Thohoyandou & Villages"
                    else
                        echo "❌ Failed to start on port $port"
                    fi
                    break
                fi
            done
            ;;
        2)
            echo "🛑 Stopping services..."
            pkill -f "community_web"
            pkill -f "python.*http.server.*8088"
            echo "✅ Services stopped"
            ;;
        3)
            echo "📊 IMPERIAL STACK STATUS"
            echo "-----------------------"
            echo "Executive Dashboard: $(nc -z localhost 8088 2>/dev/null && echo '✅' || echo '❌')"
            echo "Public Access: $(curl -s --max-time 3 monitor.humbu.store >/dev/null && echo '✅' || echo '❌')"
            echo "Automation: $(nc -z localhost 1880 2>/dev/null && echo '✅' || echo '❌')"
            echo "Sage AI: $(pgrep -f ollama >/dev/null && echo '✅' || echo '❌')"
            echo ""
            echo "💰 Financial Position: R595,238.10/month"
            echo "🏭 Industrial Backing: R412,730.15"
            echo "🎯 R5M Progress: 11.9% (59.5% to Q1 target)"
            ;;
        4)
            echo "🌐 EXECUTIVE DASHBOARD"
            echo "---------------------"
            echo "Local: http://localhost:8088"
            echo "Public: monitor.humbu.store"
            echo "Financial: http://localhost:8088/index_financial_command.html"
            echo ""
            echo "📱 Copy URL to browser"
            ;;
        5)
            echo "🔄 Running Revival Protocol..."
            nexus-revive
            ;;
        6)
            echo "🧠 Generating Sage Intelligence..."
            python3 ~/humbu_community_nexus/sage_growth_insight.py
            ;;
        7)
            echo "🌍 Testing Public Access..."
            if curl -s --max-time 5 monitor.humbu.store >/dev/null; then
                echo "✅ Public dashboard accessible"
                echo "🌐 monitor.humbu.store"
            else
                echo "❌ Public access issue - check tunnel"
                echo "🔧 Run: nexus-revive"
            fi
            ;;
        8)
            echo "📧 IDC BRIEFING PACKAGE"
            echo "----------------------"
            echo "1. Live Dashboard: monitor.humbu.store"
            echo "2. Sage Forecast: R9M by April 2026"
            echo "3. Industrial Proof: R412,730.15"
            echo "4. Recovery Protocol: nexus-revive"
            echo "5. Email: callcentre@idc.co.za"
            echo ""
            echo "Subject: Final Readiness - Humbu Imperial Stack"
            ;;
        9)
            echo "🛡️ Imperial Control terminated"
            exit 0
            ;;
        *)
            echo "❌ Invalid choice"
            ;;
    esac
    
    echo ""
    read -p "Press Enter to continue..."
    clear
    echo "🏛️ HUMBU IMPERIAL CONTROL PANEL"
    echo "================================"
    echo "IDC: #4000120009 | Sage: R9M Forecast"
    echo ""
done
