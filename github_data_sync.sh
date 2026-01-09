#!/bin/bash
# SYNC LOCAL API TO GITHUB PAGES
cd ~/humbu_community_nexus
while true; do
  git add api/*.json
  git commit -m "Imperial Pulse: $(date +'%Y-%m-%d %H:%M:%S')"
  git push https://humbulani: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@github.com/Humbulan/nexus-governance.git main
  echo "📡 Data Broadcasted to Global Dashboard."
  sleep 300  # Sync every 5 minutes to avoid GitHub rate limits
done
