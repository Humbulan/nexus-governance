#!/bin/bash
echo "🔍 TESTING MONITOR.HUMBU.STORE DOMAIN"
echo "===================================="
echo "Time: $(date '+%H:%M:%S')"
echo ""

echo "1. DNS RESOLUTION TEST:"
echo -n "   monitor.humbu.store resolves to: "
nslookup monitor.humbu.store 2>/dev/null | grep "Address:" | tail -1 | awk '{print $2}' || echo "Could not resolve"

echo ""
echo "2. HTTP/S CONNECTION TEST:"
echo -n "   http://monitor.humbu.store: "
if curl -s --max-time 10 -I http://monitor.humbu.store 2>/dev/null | head -n1 | grep -q "HTTP"; then
    echo "✅"
else
    echo "❌"
fi

echo -n "   https://monitor.humbu.store: "
if curl -s --max-time 10 -I https://monitor.humbu.store 2>/dev/null | head -n1 | grep -q "HTTP"; then
    echo "✅"
    echo "   Response: $(curl -s --max-time 5 -I https://monitor.humbu.store | head -n1)"
else
    echo "❌ (Error 1033 = DNS needs update)"
fi

echo ""
echo "3. DASHBOARD CONTENT TEST:"
if curl -s --max-time 15 "https://monitor.humbu.store/legacy_navigation.html" 2>/dev/null | grep -q "708"; then
    echo "✅ DASHBOARD SHOWS 708 MEMBERS"
    echo "🎉 DOMAIN IS WORKING!"
else
    echo "❌ DASHBOARD NOT LOADING"
    echo ""
    echo "🚨 REQUIRED ACTION:"
    echo "You MUST update Cloudflare DNS:"
    echo "1. Login to https://dash.cloudflare.com"
    echo "2. Go to humbu.store → DNS → Records"
    echo "3. Edit CNAME record for 'monitor'"
    echo "4. Set Target to: c07a0d01-7820-49d5-ac68-36e48a6b2b94.cfargotunnel.com"
    echo "5. Save and wait 3 minutes"
fi
