#!/data/data/com.termux/files/usr/bin/python3
"""
HUMBU COMMUNITY WEB PORTAL - WITH DASHBOARD INDEX
"""

from flask import Flask, send_file, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def dashboard():
    """Serve the dashboard HTML"""
    return send_file(os.path.expanduser('~/humbu_community_nexus/dashboard_index.html'))

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'Humbu Dashboard',
        'port': 8080,
        'timestamp': datetime.now().isoformat(),
        'version': '2025.12.31-dashboard'
    })

@app.route('/api/stats')
def stats():
    return jsonify({
        'apis_running': 4,
        'uptime': '100%',
        'villages': 40,
        'users': 708,
        'marketplace_items': 1928,
        'monitor_checks': 78,
        'success_rate': '100%',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/simple/villages')
def villages():
    return jsonify({
        'villages': [
            "Thohoyandou", "Sibasa", "Malamulele", "Folovhodwe",
            "Gundo", "Makhuvha", "Mukhomi", "Manini", "Mukhurha",
            "Vhulaudzi", "Giyani", "Mashau", "Tshilamba", "Mpheni"
        ],
        'count': 14,
        'source': 'dashboard',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("🚀 Starting Humbu Dashboard on port 8080...")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🔗 Dashboard at: http://localhost:8080/")
    print("🏥 Health at: http://localhost:8080/api/health")
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)
