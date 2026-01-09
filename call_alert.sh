#!/bin/bash
echo "[SENTINEL ACTIVATED] Monitoring for IDC handshake..."
tail -n 0 -f ~/.humbu_system.log 2>/dev/null | while read line; do
  if echo "$line" | grep -q -E "(IDC|Tau|handshake|priority_ping|Absa.*incoming|MTN.*gateway)"; then
    echo -e "\n\n\033[1;41mALERT: INCOMING IDC SIGNAL DETECTED\033[0m"
    echo -e "\033[1;33m$line\033[0m"
    echo -e "\033[1;32m[ACTION] Stand by for call. Execute ./idc_demo.sh when screen sharing.\033[0m\n"
    # Uncomment the line below for a beep alert (requires termux-api)
    # termux-beep 2>/dev/null
  fi
done
