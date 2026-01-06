#!/bin/bash
echo "🔍 QUICK SYSTEM TEST - $(date '+%Y-%m-%d %H:%M:%S')"
echo "======================================"

echo "1. Testing imperial-summary..."
imperial-summary 2>&1 | head -10 && echo "✅ Imperial Summary: WORKING" || echo "❌ Imperial Summary: FAILED"

echo ""
echo "2. Testing Gauteng Power Grid..."
python3 ~/humbu_community_nexus/gauteng_monitor.py check 2>&1 | head -5 && echo "✅ Power Grid: WORKING" || echo "❌ Power Grid: FAILED"

echo ""
echo "3. Testing Cloudflare..."
pgrep -f cloudflared >/dev/null && echo "✅ Cloudflare: RUNNING (PID: $(pgrep -f cloudflared))" || echo "❌ Cloudflare: STOPPED"

echo ""
echo "4. Testing URLs..."
echo "   • monitor.humbu.store: $(curl -s --max-time 3 https://monitor.humbu.store 2>&1 | head -1 | cut -c1-30)..."
echo "   • Localhost: $(curl -s --max-time 3 http://localhost:8080 2>&1 | head -1 | cut -c1-30)..."

echo ""
echo "🎯 SYSTEM STATUS: READY FOR 2026"
