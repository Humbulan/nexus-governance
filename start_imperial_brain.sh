#!/bin/bash
# AUTO-START IMPERIAL BRAIN
echo "🏛️ Starting Imperial Brain..." > ~/humbu_community_nexus/startup.log

# Start Ollama server
ollama serve >> ~/humbu_community_nexus/ollama_server.log 2>&1 &
echo "✅ Ollama server started" >> ~/humbu_community_nexus/startup.log
sleep 7

# Start Llama model
ollama run llama3.2:1b "Imperial Brain online at $(date '+%H:%M')" >> ~/humbu_community_nexus/ai_startup.log 2>&1 &
echo "✅ Llama 3.2 model loaded" >> ~/humbu_community_nexus/startup.log

# Start dashboard
cd ~/humbu_community_nexus && python3 -m http.server 8088 >> ~/humbu_community_nexus/dashboard.log 2>&1 &
echo "✅ Dashboard started on port 8088" >> ~/humbu_community_nexus/startup.log

echo "🎯 Imperial Stack started at $(date '+%H:%M')" >> ~/humbu_community_nexus/startup.log
echo "System ready for IDC presentation"
