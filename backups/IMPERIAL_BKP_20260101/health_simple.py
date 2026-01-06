#!/data/data/com.termux/files/usr/bin/python3
"""
ULTRA-SIMPLE HEALTH API - NO DEPENDENCIES
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health' or self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            response = json.dumps({
                'status': 'healthy',
                'service': 'Humbu Health Simple',
                'port': 9090,
                'timestamp': datetime.now().isoformat()
            })
            
            self.wfile.write(response.encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass

print("🚀 Starting SIMPLE Health API on port 9090...")
print("📅", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("🔗 Access: http://localhost:9090/health")
server = HTTPServer(('0.0.0.0', 9090), HealthHandler)
server.serve_forever()
