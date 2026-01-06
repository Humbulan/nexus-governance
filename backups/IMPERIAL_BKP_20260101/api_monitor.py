import sqlite3, json, os
from http.server import BaseHTTPRequestHandler, HTTPServer

# Points directly to your main project folder
BASE_DIR = os.path.expanduser('~/humbu_community_nexus')
DB_PATH = os.path.join(BASE_DIR, 'community_nexus.db')
JSON_PATH = os.path.join(BASE_DIR, 'live_tx.json')

class MonitorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT amount, msisdn, timestamp FROM transactions WHERE status='SUCCESSFUL' ORDER BY timestamp DESC LIMIT 1")
            row = cursor.fetchone()
            conn.close()
            data = {"amount": row[0], "phone": row[1], "time": row[2]} if row else {"amount": 0}
            with open(JSON_PATH, 'w') as f:
                json.dump(data, f)
            self.wfile.write(json.dumps(data).encode())
        except Exception as e:
            self.wfile.write(json.dumps({"error": str(e)}).encode())

print("Humbu Monitor Active on Port 8090...")
HTTPServer(('0.0.0.0', 8090), MonitorHandler).serve_forever()
