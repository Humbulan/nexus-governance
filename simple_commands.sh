#!/bin/bash
# Ultra-simple humbu commands

# Revenue in one line
echo "💰 R$(grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log 2>/dev/null | xargs -I {} bash -c 'echo "{} * 8.5" | bc' 2>/dev/null || echo "0")"

# Or even simpler
alias money='grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log 2>/dev/null | awk "{print \"💰 R\" \$1 * 8.5}"'
