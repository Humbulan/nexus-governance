#!/bin/bash
# Imperial Herald Quick Commands
# CEO: Humbulani Mudau

cd ~/humbu_community_nexus

case "$1" in
    morning|05:00|am)
        python3 imperial_herald.py --morning
        ;;
    evening|18:00|pm|audit)
        python3 imperial_herald.py --evening
        ;;
    status|check)
        python3 imperial_herald.py
        ;;
    *)
        echo "🏛️ Imperial Herald Commands:"
        echo "  ./herald_commands.sh morning    - Generate morning broadcast"
        echo "  ./herald_commands.sh evening    - Generate evening audit"
        echo "  ./herald_commands.sh status     - Check system status"
        echo ""
        echo "💰 Monthly Data Revenue: R103,646"
        echo "🌐 Dashboard: https://monitor.humbu.store/weather"
        ;;
esac
