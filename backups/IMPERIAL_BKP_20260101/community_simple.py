#!/data/data/com.termux/files/usr/bin/python3
"""
ULTRA-SIMPLE COMMUNITY WEB - NO DEPENDENCIES
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime

class CommunityHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        if self.path == '/api/gauteng':
            response = json.dumps({
                'status': 'initialized',
                'target': 5000000,
                'readiness': 66.9,
                'timestamp': datetime.now().isoformat()
            })
        elif self.path == '/api/services':
            response = json.dumps({
                'services': [
                    {'name': 'Street Cleaning', 'count': 160},
                    {'name': 'Water Leak Reporting', 'count': 120},
                    {'name': 'Delivery Assistance', 'count': 120},
                    {'name': 'Local Survey', 'count': 100},
                    {'name': 'Crop Monitoring', 'count': 100}
                ],
                'timestamp': datetime.now().isoformat()
            })
        elif self.path == '/api/transactions/latest':
            response = json.dumps({
                'transactions': [
                    {'village': 'Thohoyandou', 'amount': 450.00, 'timestamp': datetime.now().isoformat()},
                    {'village': 'Sibasa', 'amount': 300.00, 'timestamp': datetime.now().isoformat()},
                    {'village': 'Malamulele', 'amount': 200.00, 'timestamp': datetime.now().isoformat()}
                ],
                'count': 3,
                'timestamp': datetime.now().isoformat()
            })
        elif self.path == '/api/revenue':
            response = json.dumps({
                'today': 0,
                'weekly': 6687.34,
                'monthly_target': 28660.03,
                'progress': 100.0,
                'timestamp': datetime.now().isoformat()
            })
        else:
            response = json.dumps({
                'status': 'online',
                'service': 'Humbu Community Simple',
                'port': 8080,
                'endpoints': [
                    '/api/gauteng',
                    '/api/services', 
                    '/api/transactions/latest',
                    '/api/revenue'
                ],
                'timestamp': datetime.now().isoformat()
            })
        
        self.wfile.write(response.encode())
    
    def log_message(self, format, *args):
        pass

print("🚀 Starting SIMPLE Community Web on port 8080...")
print("📅", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("🔗 Available endpoints:")
print("   /api/gauteng")
print("   /api/services")
print("   /api/transactions/latest")
print("   /api/revenue")
server = HTTPServer(('0.0.0.0', 8080), CommunityHandler)
server.serve_forever()
