#!/bin/bash
# SIMPLE TUNNEL STARTER - FIXED
echo "🌐 Starting Cloudflare tunnel with fixed credentials..."

# Kill any existing tunnel
pkill -f cloudflared 2>/dev/null
sleep 2

# Use ABSOLUTE path to credentials
CREDENTIALS_FILE="/data/data/com.termux/files/home/.cloudflared/c07a0d01-7820-49d5-ac68-36e48a6b2b94.json"

if [ -f "$CREDENTIALS_FILE" ]; then
    echo "✅ Credentials file found"
    echo "Starting tunnel to monitor.humbu.store..."
    
    # Start tunnel with absolute paths
    cloudflared tunnel --credentials-file "$CREDENTIALS_FILE" --url http://localhost:8088 run c07a0d01-7820-49d5-ac68-36e48a6b2b94 &
    TUNNEL_PID=$!
    
    echo "✅ Tunnel started with PID: $TUNNEL_PID"
    echo "Domain: https://monitor.humbu.store"
    echo "Note: Takes 30-60 seconds to establish"
    
    # Wait and check
    sleep 40
    echo ""
    echo "🔍 Checking connection..."
    if curl -s -I https://monitor.humbu.store 2>/dev/null | head -1 | grep -q "200"; then
        echo "🎉 SUCCESS: monitor.humbu.store is LIVE!"
    else
        echo "⚠️ Still connecting... Check again in 30 seconds"
    fi
else
    echo "❌ Credentials file not found at: $CREDENTIALS_FILE"
    echo "Available credentials:"
    ls -la ~/.cloudflared/*.json 2>/dev/null | head -5
fi
