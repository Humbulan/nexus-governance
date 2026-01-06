#! /usr/bin/env python3
#!/usr/bin/env python3
"""
Enhanced Revenue Engine - Unified Dashboard Server
Serves all Humbu dashboards from port 8086
"""

from flask import Flask, request, jsonify, render_template_string
import json
import time
import os
from datetime import datetime

app = Flask(__name__)

# HTML templates for different dashboards
MONITOR_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Humbu Monitor</title>
    <style>body{font-family:Arial;padding:20px;background:#f5f5f5;}</style>
</head>
<body>
    <h1>🚀 Humbu Monitoring Dashboard</h1>
    <p>Village #41 - Status: <strong>ACTIVE</strong></p>
    <p>Port: 8086 | Time: {{timestamp}}</p>
    <div id="data">{{data}}</div>
</body>
</html>
'''

LIVE_MAP_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Live Map</title>
    <style>body{font-family:Arial;padding:20px;background:#000;color:#0f0;}</style>
</head>
<body>
    <h1>🗺️ Live Map Dashboard</h1>
    <p>Real-time monitoring active</p>
    <p>Last update: {{timestamp}}</p>
</body>
</html>
'''

DASHBOARD_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Fixed Dashboard</title>
    <style>body{font-family:Arial;padding:20px;background:#1a1a1a;color:#fff;}</style>
</head>
<body>
    <h1>📊 Fixed Dashboard</h1>
    <p>Revenue Engine: <span style="color:#4CAF50;">RUNNING</span></p>
    <p>Port: 8086 | Host: {{hostname}}</p>
</body>
</html>
'''

@app.route('/')
def home():
    """Main endpoint - detects which dashboard is being accessed"""
    hostname = request.headers.get('Host', '')
    
    if 'monitor' in hostname:
        return render_template_string(MONITOR_TEMPLATE, 
                                     timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                     data=json.dumps({"status": "active", "village": 41}))
    
    elif 'live-map' in hostname:
        return render_template_string(LIVE_MAP_TEMPLATE,
                                     timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    elif 'fixed-dashbox' in hostname or 'village' in hostname:
        return render_template_string(DASHBOARD_TEMPLATE,
                                     hostname=hostname)
    
    # Default JSON response for API calls
    return jsonify({
        "status": "active",
        "service": "humbu-revenue-engine",
        "port": 8086,
        "timestamp": time.time(),
        "village": 41,
        "endpoints": ["/", "/health", "/api/revenue", "/api/status"],
        "supported_dashboards": [
            "monitor.humbu.store",
            "live-map.humbu.store", 
            "fixed-dashbox.humbu.store",
            "village.humbu.store"
        ]
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "port": 8086,
        "memory": "stable"
    })

@app.route('/api/status')
def status():
    """Status endpoint for all dashboards"""
    return jsonify({
        "server": "humbu-unified-dashboard",
        "version": "2.0",
        "port": 8086,
        "uptime": "active",
        "dashboards_served": 4,
        "timestamp": time.time()
    })

if __name__ == '__main__':
    print("🚀 Enhanced Revenue Engine starting on port 8086...")
    print("📊 Serving all Humbu dashboards:")
    print("   • monitor.humbu.store")
    print("   • live-map.humbu.store")
    print("   • fixed-dashbox.humbu.store")
    print("   • village.humbu.store")
    print("🔗 Running on: http://0.0.0.0:8086")
    
    # Run on all interfaces, port 8086
    app.run(host='0.0.0.0', port=8086, debug=False)
