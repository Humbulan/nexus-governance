#!/bin/bash
echo "🔄 ATTEMPTING AUTOMATED DNS FIX..."
echo "Tunnel ID: c07a0d01-7820-49d5-ac68-36e48a6b2b94"

# Try to delete conflicting record
echo "1. Attempting to delete conflicting DNS record..."
cloudflared tunnel route dns delete humbu-imperial monitor.humbu.store 2>&1 | tee /tmp/dns_delete.log

sleep 2

# Try to create correct record
echo "2. Creating correct DNS record..."
cloudflared tunnel route dns humbu-imperial monitor.humbu.store 2>&1 | tee /tmp/dns_create.log

# Check results
if grep -q "Success" /tmp/dns_create.log; then
    echo "✅ AUTOMATED DNS FIX SUCCESSFUL!"
    echo "Wait 2-3 minutes for propagation"
    echo "Then test: https://monitor.humbu.store"
else
    echo "❌ AUTOMATED FIX FAILED"
    echo ""
    echo "🚨 MANUAL INTERVENTION REQUIRED:"
    echo "You MUST login to Cloudflare Dashboard and:"
    echo "1. Find CNAME record for 'monitor'"
    echo "2. Change Target to: c07a0d01-7820-49d5-ac68-36e48a6b2b94.cfargotunnel.com"
    echo "3. Save and wait 3 minutes"
fi
