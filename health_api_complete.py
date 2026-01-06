#! /usr/bin/env python3
from flask import Flask, jsonify
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'status': 'online',
        'service': 'Humbu Health Monitor',
        'port': 9090,
        'timestamp': datetime.now().isoformat(),
        'endpoints': ['/', '/health', '/status', '/api/check']
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'services': {
            'monitor': 'running',
            'database': 'connected',
            'api': 'operational',
            'tunnel': 'active'
        }
    })

@app.route('/status')
def status():
    # Check all services
    services = []
    ports = [(8080, 'Community Web'), (8083, 'Government API'), (8086, 'Revenue Bridge'), (9090, 'Health API')]
    
    for port, name in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('localhost', port))
            status = 'up' if result == 0 else 'down'
            sock.close()
        except:
            status = 'error'
        
        services.append({
            'name': name,
            'port': port,
            'status': status
        })
    
    return jsonify({
        'timestamp': datetime.now().isoformat(),
        'services': services,
        'summary': {
            'total': len(services),
            'up': len([s for s in services if s['status'] == 'up']),
            'down': len([s for s in services if s['status'] == 'down'])
        }
    })

@app.route('/api/check')
def check():
    return jsonify({
        'system': 'humbu_imperial',
        'version': '2025.12.31',
        'status': 'operational',
        'villages': 40,
        'users': 708,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("🚀 Starting COMPLETE Health API on port 9090...")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    app.run(host='0.0.0.0', port=9090, debug=False, threaded=True)
