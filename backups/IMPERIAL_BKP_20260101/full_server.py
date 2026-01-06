from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime
import os

class FullHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Handle HTML requests
        if self.path == '/' or self.path.endswith('.html'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            
            if self.path == '/':
                # Serve the beautiful dashboard
                with open(os.path.expanduser('~/humbu_community_nexus/index.html'), 'rb') as f:
                    self.wfile.write(f.read())
            else:
                # Try to serve other HTML files
                try:
                    with open(os.path.expanduser('~' + self.path), 'rb') as f:
                        self.wfile.write(f.read())
                except:
                    self.send_error(404, "File not found")
            return
        
        # Handle API requests (JSON)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        now = datetime.now()
        
        if self.path == '/health':
            response = {
                'status': 'healthy',
                'service': 'Humbu Community Nexus',
                'timestamp': now.isoformat(),
                'message': 'Dashboard and APIs fully operational',
                'version': '2026.1.0'
            }
        elif self.path == '/api/gauteng':
            response = {
                'region': 'Gauteng Province',
                'status': 'expansion_active',
                'target_amount': 5000000,
                'readiness_percentage': 66.9,
                'villages_monitored': 40,
                'timestamp': now.isoformat()
            }
        elif self.path == '/api/services':
            response = {
                'services': [
                    {'name': 'Street Cleaning', 'active_villages': 160, 'status': 'active'},
                    {'name': 'Water Leak Reporting', 'active_villages': 120, 'status': 'active'},
                    {'name': 'Delivery Assistance', 'active_villages': 120, 'status': 'active'},
                    {'name': 'Local Survey', 'active_villages': 100, 'status': 'active'},
                    {'name': 'Crop Monitoring', 'active_villages': 100, 'status': 'active'}
                ],
                'total_active_services': 5,
                'timestamp': now.isoformat()
            }
        elif self.path == '/api/transactions/latest':
            response = {
                'transactions': [
                    {'id': 'TX2026001', 'village': 'Thohoyandou', 'amount': 450.00, 'type': 'payment', 'status': 'completed'},
                    {'id': 'TX2026002', 'village': 'Sibasa', 'amount': 300.00, 'type': 'payment', 'status': 'completed'},
                    {'id': 'TX2026003', 'village': 'Malamulele', 'amount': 200.00, 'type': 'payment', 'status': 'completed'}
                ],
                'daily_total': 950.00,
                'currency': 'ZAR',
                'timestamp': now.isoformat()
            }
        elif self.path == '/api/revenue':
            response = {
                'revenue_summary': {
                    'today': 950.00,
                    'this_week': 6687.34,
                    'this_month_target': 28660.03,
                    'monthly_progress': 100.0,
                    'average_daily': 955.33
                },
                'timestamp': now.isoformat()
            }
        else:
            response = {
                'error': 'Endpoint not found',
                'available': [
                    '/',
                    '/health',
                    '/api/gauteng',
                    '/api/services',
                    '/api/transactions/latest',
                    '/api/revenue'
                ],
                'timestamp': now.isoformat()
            }
        
        self.wfile.write(json.dumps(response, indent=2).encode())
    
    def log_message(self, format, *args):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {self.client_address[0]} - {self.path}")

# Restart server on port 8080
print("🚀 LAUNCHING FULL DASHBOARD + API SERVER")
print(f"⏰ Time: {datetime.now().strftime('%H:%M:%S')}")
print("🔗 YOUR MEETING URL: https://trim-tires-martin-grande.trycloudflare.com/")
print("📱 Beautiful HTML dashboard + All JSON APIs")
print("")
print("✅ Endpoints available:")
print("   • /              (HTML Dashboard)")
print("   • /health        (Health Check)")
print("   • /api/gauteng   (Gauteng API)")
print("   • /api/services  (Services API)")
print("   • /api/transactions/latest")
print("   • /api/revenue")

server = HTTPServer(('0.0.0.0', 8080), FullHandler)
server.serve_forever()
