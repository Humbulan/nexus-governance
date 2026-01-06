#! /usr/bin/env python3
from flask import Flask, jsonify
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def home(): return jsonify({'status':'online','service':'Gov API','port':8083})
@app.route('/health')
def health(): return jsonify({'status':'healthy','timestamp':datetime.now().isoformat()})
if __name__ == '__main__':
    print("Starting Government API on 8083...")
    app.run(host='0.0.0.0', port=8083, debug=False)
