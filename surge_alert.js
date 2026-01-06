// SURGE PROTOCOL: R600k Alert System
setInterval(function() {
    fetch('financial_ledger.json')
        .then(response => response.json())
        .then(data => {
            if (data.net_monthly_flow >= 600000) {
                // Visual alert
                document.body.style.animation = "pulse 1s infinite";
                document.title = "🚨 REVENUE SURGE: R" + data.net_monthly_flow.toLocaleString();
                
                // Create alert banner
                if (!document.getElementById('surge-alert')) {
                    const alert = document.createElement('div');
                    alert.id = 'surge-alert';
                    alert.style.cssText = 'position:fixed; top:0; left:0; right:0; background:#d4af37; color:#000; padding:15px; text-align:center; font-weight:bold; z-index:9999;';
                    alert.innerHTML = '🚨 REVENUE SURGE DETECTED: R' + data.net_monthly_flow.toLocaleString() + ' 🚨';
                    document.body.prepend(alert);
                }
            }
        });
}, 5000); // Check every 5 seconds
