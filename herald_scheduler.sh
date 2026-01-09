#!/bin/bash
# 🏛️ Imperial Herald Scheduler
# Automates broadcasts at 05:00 and 18:00 daily

cd ~/humbu_community_nexus

HOUR=$(date +%H)

case $HOUR in
    05)
        echo "🌅 05:00 AM - Sending Morning Broadcast..."
        python3 imperial_herald.py --morning
        echo "✅ Broadcast sent to 43 villages"
        ;;
        
    18)
        echo "🌇 18:00 PM - Generating Evening Audit..."
        python3 imperial_herald.py --evening
        echo "✅ Audit generated for IDC"
        ;;
        
    *)
        echo "⏰ Imperial Herald Scheduler Active"
        echo "Next broadcast:"
        echo "  • 05:00 AM (Morning Farmer Report)"
        echo "  • 18:00 PM (Evening IDC Audit)"
        ;;
esac
