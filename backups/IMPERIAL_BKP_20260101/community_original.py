from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'service': 'Humbu Community Web',
        'status': 'online',
        'port': 8080,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/gauteng')
def gauteng():
    return jsonify({
        'status': 'initialized',
        'target': 5000000,
        'readiness': 66.9,
        'region': 'Gauteng Province',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/services')
def services():
    return jsonify({
        'services': [
            {'name': 'Street Cleaning', 'count': 160, 'active': True},
            {'name': 'Water Leak Reporting', 'count': 120, 'active': True},
            {'name': 'Delivery Assistance', 'count': 120, 'active': True},
            {'name': 'Local Survey', 'count': 100, 'active': True},
            {'name': 'Crop Monitoring', 'count': 100, 'active': True}
        ],
        'total': 600,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/transactions/latest')
def transactions():
    return jsonify({
        'transactions': [
            {'id': 1, 'village': 'Thohoyandou', 'amount': 450.00, 'type': 'payment'},
            {'id': 2, 'village': 'Sibasa', 'amount': 300.00, 'type': 'payment'},
            {'id': 3, 'village': 'Malamulele', 'amount': 200.00, 'type': 'payment'}
        ],
        'count': 3,
        'total': 950.00,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/revenue')
def revenue():
    return jsonify({
        'today': 0,
        'weekly': 6687.34,
        'monthly_target': 28660.03,
        'progress': 100.0,
        'currency': 'ZAR',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print(f"🌍 Community Web restored on port 8080 at {datetime.now().strftime('%H:%M:%S')}")
    print("📌 Available endpoints:")
    print("   /api/gauteng")
    print("   /api/services")
    print("   /api/transactions/latest")
    print("   /api/revenue")
    app.run(host='0.0.0.0', port=8080, debug=False)
