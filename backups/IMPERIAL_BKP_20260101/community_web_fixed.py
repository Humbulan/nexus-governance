#!/data/data/com.termux/files/usr/bin/python3
"""
HUMBU COMMUNITY WEB PORTAL - FIXED VERSION
Runs on port 8080 with Flask
"""

from flask import Flask, jsonify, render_template_string
import sqlite3
import os
from datetime import datetime
import json

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Humbu Community Portal</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; }
        .header { background: #2c3e50; color: white; padding: 15px; border-radius: 5px; }
        .metric { background: #ecf0f1; padding: 10px; margin: 10px 0; border-radius: 5px; }
        .status-up { color: green; }
        .status-down { color: red; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏛️ Humbu Community Portal</h1>
            <p>Real-time village intelligence dashboard</p>
        </div>
        
        <div class="metric">
            <h3>📊 System Status</h3>
            <p>API: <span class="status-up">● ONLINE</span></p>
            <p>Port: 8080</p>
            <p>Time: {{ timestamp }}</p>
        </div>
        
        <div class="metric">
            <h3>🌍 Village Network</h3>
            <p>Total Villages: {{ village_count }}</p>
            <p>Active Today: {{ active_villages }}</p>
        </div>
        
        <div class="metric">
            <h3>💰 Revenue Today</h3>
            <p>Transactions: {{ today_count }}</p>
            <p>Total: R{{ today_total }}</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    try:
        conn = sqlite3.connect(os.path.expanduser('~/humbu_community_nexus/community_nexus.db'))
        cursor = conn.cursor()
        
        # Get village count
        cursor.execute("SELECT COUNT(DISTINCT village) FROM marketplace")
        village_count = cursor.fetchone()[0] or 40
        
        # Get active villages today
        cursor.execute("SELECT COUNT(DISTINCT village) FROM transactions WHERE date(timestamp) = date('now')")
        active_villages = cursor.fetchone()[0] or 0
        
        # Get today's revenue
        cursor.execute("SELECT COUNT(*), SUM(amount) FROM transactions WHERE date(timestamp) = date('now')")
        today_result = cursor.fetchone()
        today_count = today_result[0] or 0
        today_total = today_result[1] or 0
        
        conn.close()
        
        return render_template_string(HTML_TEMPLATE, 
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            village_count=village_count,
            active_villages=active_villages,
            today_count=today_count,
            today_total=f"{today_total:,.2f}"
        )
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'Humbu Community Web',
        'port': 8080,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/villages')
def villages():
    try:
        conn = sqlite3.connect(os.path.expanduser('~/humbu_community_nexus/community_nexus.db'))
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT village FROM marketplace LIMIT 20")
        villages = [row[0] for row in cursor.fetchall()]
        conn.close()
        return jsonify({
            'villages': villages,
            'count': len(villages),
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats')
def stats():
    return jsonify({
        'villages_connected': 40,
        'active_users': 708,
        'marketplace_items': 1928,
        'weekly_revenue': 6687.34,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("🚀 Starting FIXED Humbu Community Web on port 8080...")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🔗 Access at: http://localhost:8080")
    print("🏥 Health at: http://localhost:8080/api/health")
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)
