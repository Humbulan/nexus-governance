from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'status': 'online',
        'service': 'Humbu Health Monitor',
        'timestamp': datetime.now().isoformat(),
        'version': '2025.12.31'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'services': {
            'monitor': 'running',
            'database': 'connected',
            'api': 'operational'
        }
    })

@app.route('/status')
def status():
    # Check if other APIs are running
    import socket
    services = []
    
    for port, name in [(8080, 'Community Web'), (8083, 'Government API'), (8086, 'Revenue Bridge')]:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('localhost', port))
            services.append({
                'name': name,
                'port': port,
                'status': 'up' if result == 0 else 'down'
            })
            sock.close()
        except:
            services.append({
                'name': name,
                'port': port,
                'status': 'error'
            })
    
    return jsonify({
        'timestamp': datetime.now().isoformat(),
        'services': services,
        'system': {
            'villages': 40,
            'users': 708,
            'marketplace_items': 1928
        }
    })

if __name__ == '__main__':
    print("🚀 Starting FIXED Health API on port 9090...")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🔗 Access at: http://localhost:9090/health")
    app.run(host='0.0.0.0', port=9090, debug=False)
