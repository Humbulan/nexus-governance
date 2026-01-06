#! /usr/bin/env python3
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api/gauteng')
def gauteng():
    return jsonify({
        'government_service': 'Gauteng Provincial API',
        'status': 'active',
        'departments': ['Health', 'Education', 'Transport', 'Housing'],
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/services')
def services():
    return jsonify({
        'government_services': [
            {'department': 'Public Works', 'service': 'Road Maintenance', 'status': 'active'},
            {'department': 'Water & Sanitation', 'service': 'Water Supply', 'status': 'active'},
            {'department': 'Health', 'service': 'Clinic Services', 'status': 'active'},
            {'department': 'Home Affairs', 'service': 'ID Applications', 'status': 'active'}
        ],
        'timestamp': datetime.now().isoformat()
    })

@app.route('/')
def index():
    return jsonify({
        'service': 'Government API - Original',
        'port': 8083,
        'status': 'online',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print(f"🏛️ Government API restored on port 8083 at {datetime.now().strftime('%H:%M:%S')}")
    print("🔗 Access: http://localhost:8083/api/gauteng")
    app.run(host='0.0.0.0', port=8083, debug=False)
