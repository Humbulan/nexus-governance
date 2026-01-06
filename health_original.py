#! /usr/bin/env python3
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'Humbu Health API',
        'timestamp': datetime.now().isoformat(),
        'port': 9090,
        'version': '1.0.0'
    })

@app.route('/')
def home():
    return jsonify({
        'message': 'Health API - Original Restored',
        'endpoints': ['/health'],
        'status': 'online'
    })

if __name__ == '__main__':
    print(f"🏥 Health API restored on port 9090 at {datetime.now().strftime('%H:%M:%S')}")
    print("🔗 Access: http://localhost:9090/health")
    app.run(host='0.0.0.0', port=9090, debug=False)
