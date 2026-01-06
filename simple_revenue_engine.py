#! /usr/bin/env python3
#!/usr/bin/env python3
# 🏛️ SIMPLE ROBUST REVENUE ENGINE

from flask import Flask, jsonify
from datetime import datetime
import sys

app = Flask(__name__)

# Updated revenue data with Malamulele East
REVENUE_DATA = {
    "monthly_target": 28660.03,
    "progress": 99.99999639990358,
    "timestamp": datetime.now().isoformat(),
    "today": 0,
    "weekly": 6687.339759249312,
    "total_realized": 445895.16 + 12500.00,  # Includes Malamulele East
    "target": 5000000.00,
    "currency": "ZAR",
    "status": "active"
}

@app.route('/')
def home():
    return jsonify({"service": "Revenue Bridge", "status": "active", "port": 8086})

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "timestamp": str(datetime.now())}), 200

@app.route('/api/revenue')
def revenue():
    return jsonify(REVENUE_DATA)

@app.route('/api/stats')
def stats():
    return jsonify({
        "active_users": 708,
        "marketplace_items": 1928,
        "timestamp": datetime.now().isoformat(),
        "villages_connected": 41,  # Updated with Malamulele East
        "weekly_revenue": 6687.34,
        "villages": [
            {"name": "Malamulele East", "revenue": 12500.00, "status": "active"},
            {"name": "Sibasa Central", "revenue": 8500.00, "status": "active"},
            {"name": "Thohoyandou Hub", "revenue": 10200.00, "status": "active"}
        ]
    })

@app.route('/api/villages')
def villages():
    return jsonify([
        {"name": "Malamulele East", "revenue": 12500.00, "added": "2026-01-02", "region": "Limpopo"},
        {"name": "Sibasa Central", "revenue": 8500.00, "added": "2026-01-01", "region": "Limpopo"},
        {"name": "Thohoyandou Hub", "revenue": 10200.00, "added": "2025-12-30", "region": "Limpopo"}
    ])

if __name__ == '__main__':
    print(f"🚀 Starting SIMPLE Revenue Engine on port 8086...")
    print(f"📅 {datetime.now()}")
    print(f"💰 Total Revenue: R{REVENUE_DATA['total_realized']:.2f} (includes Malamulele East)")
    
    try:
        app.run(host='0.0.0.0', port=8086, debug=False, threaded=True)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ ERROR: Port 8086 already in use")
            print(f"💡 Try: pkill -f 'simple_revenue_engine'")
            print(f"💡 Or check: curl http://localhost:8086/")
        else:
            print(f"❌ ERROR: {e}")
