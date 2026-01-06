from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api/transactions/latest')
def transactions():
    return jsonify({
        'transactions': [
            {'id': 'TX001', 'amount': 450.00, 'status': 'completed', 'village': 'Thohoyandou'},
            {'id': 'TX002', 'amount': 300.00, 'status': 'completed', 'village': 'Sibasa'},
            {'id': 'TX003', 'amount': 200.00, 'status': 'completed', 'village': 'Malamulele'}
        ],
        'bridge': 'Revenue Bridge API',
        'total_today': 950.00,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/revenue')
def revenue():
    return jsonify({
        'revenue_data': {
            'today': 950.00,
            'this_week': 6687.34,
            'this_month': 28660.03,
            'target': 50000.00,
            'progress': 57.32
        },
        'currency': 'ZAR',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/')
def index():
    return jsonify({
        'service': 'Revenue Bridge - Original',
        'port': 8086,
        'status': 'online',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print(f"💰 Revenue Bridge restored on port 8086 at {datetime.now().strftime('%H:%M:%S')}")
    print("🔗 Access: http://localhost:8086/api/transactions/latest")
    app.run(host='0.0.0.0', port=8086, debug=False)
