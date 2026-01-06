#!/bin/bash
echo "🔍 GATEWAY STATUS CHECK"
echo "======================="

if curl -s http://localhost:8083/ > /dev/null; then
    echo "✅ Gateway ONLINE at http://localhost:8083/"
    curl -s http://localhost:8083/ | python3 -m json.tool
else
    echo "❌ Gateway OFFLINE"
    echo ""
    echo "To start gateway:"
    echo "cd ~/humbu_community_nexus"
    echo "python3 working_gateway.py &"
    echo ""
    echo "Or use the backup generator:"
    echo "./backup_generator.sh"
fi
