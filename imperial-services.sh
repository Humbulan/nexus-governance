#!/bin/bash
# 🏛️ Imperial Services Manager

case "$1" in
    start)
        echo "🏛️ Starting Imperial Services..."
        
        # Ollama
        if ! pgrep -f "ollama serve" > /dev/null; then
            ollama serve > ~/humbu_community_nexus/ollama.log 2>&1 &
            echo "🤖 Ollama server started"
        fi
        
        # Wait for Ollama
        sleep 8
        
        # Llama model
        if ! ollama ps 2>/dev/null | grep -q "llama3.2:1b"; then
            ollama run llama3.2:1b "Imperial online" > ~/humbu_community_nexus/ai.log 2>&1 &
            echo "🧠 Llama 3.2 model loading..."
        fi
        
        # Dashboard
        if ! pgrep -f "http.server 8088" > /dev/null; then
            cd ~/humbu_community_nexus && python3 -m http.server 8088 > ~/humbu_community_nexus/web.log 2>&1 &
            echo "📊 Dashboard started on port 8088"
        fi
        
        # Tunnel
        if ! pgrep -f "cloudflared tunnel" > /dev/null; then
            cloudflared tunnel run > ~/humbu_community_nexus/tunnel.log 2>&1 &
            echo "🌐 Cloudflare tunnel started"
        fi
        
        echo "✅ All services started"
        ;;
    
    stop)
        echo "🛑 Stopping Imperial Services..."
        pkill -f ollama
        pkill -f "python3 -m http.server"
        pkill -f cloudflared
        pkill -f node-red
        echo "✅ All services stopped"
        ;;
    
    status)
        echo "🏛️ Imperial Services Status:"
        echo "============================"
        
        # Check each service
        services=("ollama" "python3" "cloudflared" "node-red")
        for service in "${services[@]}"; do
            if pgrep -f "$service" > /dev/null; then
                echo "✅ $service: RUNNING"
            else
                echo "❌ $service: STOPPED"
            fi
        done
        
        # Special check for Llama model
        if ollama ps 2>/dev/null | grep -q "llama3.2:1b"; then
            echo "✅ Llama 3.2: LOADED IN RAM"
        else
            echo "❌ Llama 3.2: NOT LOADED"
        fi
        
        # Check dashboard
        if curl -s http://localhost:8088 > /dev/null 2>&1; then
            echo "✅ Dashboard: ACCESSIBLE"
            echo "🌐 Public URL: monitor.humbu.store"
        else
            echo "❌ Dashboard: NOT ACCESSIBLE"
        fi
        ;;
    
    restart)
        echo "🔄 Restarting Imperial Services..."
        $0 stop
        sleep 3
        $0 start
        ;;
    
    logs)
        echo "📋 Service Logs:"
        echo "1. Ollama: ~/humbu_community_nexus/ollama.log"
        echo "2. Dashboard: ~/humbu_community_nexus/web.log"
        echo "3. Tunnel: ~/humbu_community_nexus/tunnel.log"
        echo "4. AI Model: ~/humbu_community_nexus/ai.log"
        echo ""
        echo "Use: tail -f ~/humbu_community_nexus/[logfile]"
        ;;
    
    *)
        echo "Usage: $0 {start|stop|status|restart|logs}"
        echo ""
        echo "Imperial Services Manager"
        echo "Controls the entire Humbu Imperial Stack"
        exit 1
        ;;
esac
