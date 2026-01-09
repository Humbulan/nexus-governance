#!/bin/bash
echo "🛡️ IMPERIAL AUDIT WATCHDOG ACTIVATED - $(date)"
echo "Monitoring Quad-Link Protocol for IDC access"
echo ""

# Create uptime log
UPTIME_LOG="$HOME/humbu_community_nexus/uptime.log"
echo "=== AUDIT WATCHDOG STARTED $(date) ===" > "$UPTIME_LOG"

# Critical URLs to monitor
CRITICAL_URLS=(
  "https://monitor.humbu.store/master"
  "https://monitor.humbu.store/live"
  "https://monitor.humbu.store/"
  "https://monitor.humbu.store/complete"
)

while true; do
  TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
  ALL_UP=true
  
  echo "[$TIMESTAMP] Checking Quad-Link Status..." >> "$UPTIME_LOG"
  
  for url in "${CRITICAL_URLS[@]}"; do
    # Extract just the path for logging
    path=$(echo "$url" | cut -d'/' -f4-)
    
    if curl -s --max-time 10 --head "$url" 2>/dev/null | grep -q "200 OK"; then
      echo "  ✅ $path: ACTIVE" >> "$UPTIME_LOG"
    else
      echo "  ⚠️  $path: DOWN - Attempting recovery..." >> "$UPTIME_LOG"
      ALL_UP=false
      
      # Recovery actions based on URL
      case "$path" in
        "master"|"live"|""|"complete")
          echo "  🔄 Restarting multi_dashboard_server.py..." >> "$UPTIME_LOG"
          pkill -f "multi_dashboard_server.py"
          cd ~/humbu_community_nexus
          nohup python3 multi_dashboard_server.py > ~/.imperial_portal.log 2>&1 &
          ;;
      esac
    fi
  done
  
  if $ALL_UP; then
    echo "[$TIMESTAMP] ✅ ALL QUAD-LINKS OPERATIONAL" >> "$UPTIME_LOG"
  else
    echo "[$TIMESTAMP] ⚠️  SOME LINKS REQUIRED RECOVERY" >> "$UPTIME_LOG"
  fi
  
  # Log system status
  echo "  📊 System: multi_dashboard_server.py $(ps aux | grep -q 'multi_dashboard_server' && echo 'RUNNING' || echo 'STOPPED')" >> "$UPTIME_LOG"
  echo "  🌐 Cloudflare: $(ps aux | grep -q 'cloudflared' && echo 'ACTIVE' || echo 'INACTIVE')" >> "$UPTIME_LOG"
  
  # Wait 60 seconds before next check
  sleep 60
done
