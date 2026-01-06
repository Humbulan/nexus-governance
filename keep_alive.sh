#!/bin/bash
while true; do
    # Check local server
    if ! pgrep -f "python.*http.server" > /dev/null; then
        echo "🔄 Restarting local server..."
        cd ~/humbu_community_nexus
        python3 -m http.server 8088 --bind 0.0.0.0 &
    fi
    
    # Check tunnel
    if ! pgrep -f cloudflared > /dev/null; then
        echo "🔄 Restarting tunnel..."
        cloudflared tunnel run c07a0d01-7820-49d5-ac68-36e48a6b2b94 &
    fi
    
    # Status
    echo "✅ System running - $(date '+%H:%M:%S')"
    echo "   Domain: https://monitor.humbu.store"
    echo "   Local: http://localhost:8088"
    echo ""
    
    sleep 60  # Check every minute
done

    # Check AI Brain (Ollama)
    if ! pgrep -f ollama > /dev/null; then
        echo "🔄 Restarting AI Brain..."
        export OLLAMA_MODELS=/data/data/com.termux/files/home/humbu-enterprise-platform/Models/models
        nohup ollama serve > ~/logs/ollama_auto.log 2>&1 &
    fi
