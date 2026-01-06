#!/data/data/com.termux/files/usr/bin/python3
"""
HUMBU COMMUNITY WEB - COMPLETE VERSION
"""

from flask import Flask, jsonify, send_file
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def dashboard():
    """Serve the dashboard HTML if it exists, else show API info"""
    dashboard_path = os.path.expanduser('~/humbu_community_nexus/dashboard_index.html')
    if os.path.exists(dashboard_path):
        return send_file(dashboard_path)
    else:
        return jsonify({
            'status': 'online',
            'service': 'Humbu Community Web',
            'port': 8080,
            'timestamp': datetime.now().isoformat(),
            'endpoints': ['/', '/health', '/api/stats', '/api/villages', '/api/services'],
            'message': 'Dashboard HTML not found, serving API mode'
        })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'Humbu Community Web',
        'port': 8080,
        'timestamp': datetime.now().isoformat(),
        'version': '2025.12.31-complete'
    })

@app.route('/api/stats')
def stats():
    return jsonify({
        'apis_running': 4,
        'uptime': '100%',
        'villages': 40,
        'users': 708,
        'marketplace_items': 1928,
        'weekly_revenue': 6687.34,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/villages')
def villages():
    return jsonify({
        'villages': [
            "Thohoyandou", "Sibasa", "Malamulele", "Folovhodwe",
            "Gundo", "Makhuvha", "Mukhomi", "Manini", "Mukhurha",
            "Vhulaudzi", "Giyani", "Mashau", "Tshilamba", "Mpheni"
        ],
        'count': 14,
        'active': 40,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/services')
def services():
    return jsonify({
        'services': [
            {'name': 'Marketplace', 'status': 'active', 'items': 1928},
            {'name': 'USSD Gateway', 'status': 'active', 'code': '*134*600#'},
            {'name': 'Mobile Money', 'status': 'active', 'provider': 'MTN MoMo'},
            {'name': 'Logistics', 'status': 'active', 'vehicles': 17},
            {'name': 'Monitoring', 'status': 'active', 'checks': 78}
        ],
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("🚀 Starting COMPLETE Community Web on port 8080...")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🔗 Available endpoints:")
    print("   /              - Dashboard/API home")
    print("   /health        - Health check")
    print("   /api/stats     - System statistics")
    print("   /api/villages  - Village list")
    print("   /api/services  - Services list")
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)
