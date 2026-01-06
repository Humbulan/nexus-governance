from flask import Flask, jsonify
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def home(): return jsonify({'status':'online','service':'Revenue Bridge','port':8086})
@app.route('/health')
def health(): return jsonify({'status':'healthy','timestamp':datetime.now().isoformat()})
@app.route('/revenue')
def revenue(): return jsonify({'today':0,'weekly':6687.34,'target':28660.03})
if __name__ == '__main__':
    print("Starting Revenue Bridge on 8086...")
    app.run(host='0.0.0.0', port=8086, debug=False)
