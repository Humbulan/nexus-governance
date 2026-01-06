import http.server
import socketserver
import json
import time
import os

class ImperialRequestHandler(http.server.SimpleHTTPRequestHandler):
    def send_no_cache_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    
    def do_GET(self):
        # Force fresh fleet data with timestamp
        if self.path == '/fleet_data.json' or self.path == '/fleet_telemetry.json':
            try:
                with open('fleet_data.json', 'r') as f:
                    data = json.load(f)
                
                # Update timestamp to force new data
                current_time = time.strftime('%Y-%m-%dT%H:%M:%S.%fZ', time.gmtime())
                data['last_update'] = current_time
                data['timestamp'] = int(time.time())
                if 'metrics' in data:
                    data['metrics']['last_system_update'] = time.strftime('%H:%M:%S')
                
                # Update individual vehicle timestamps
                for vehicle in data.get('fleet', []):
                    vehicle['last_update'] = time.strftime('%H:%M:%S')
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_no_cache_headers()
                self.end_headers()
                
                self.wfile.write(json.dumps(data).encode())
                print(f"[IMPERIAL] {time.strftime('%H:%M:%S')} - Sent fresh fleet data")
                return
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
                return
        
        # Serve other files with no cache
        self.send_response(200)
        if self.path.endswith('.html'):
            self.send_header('Content-type', 'text/html')
        elif self.path.endswith('.css'):
            self.send_header('Content-type', 'text/css')
        elif self.path.endswith('.js'):
            self.send_header('Content-type', 'application/javascript')
        else:
            self.send_header('Content-type', 'text/plain')
        
        self.send_no_cache_headers()
        self.end_headers()
        
        # Serve the file
        try:
            if self.path == '/':
                path = 'index.html'
            else:
                path = self.path[1:]  # Remove leading slash
            
            if os.path.exists(path):
                with open(path, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(b'File not found')
        except Exception as e:
            self.wfile.write(f'Error: {str(e)}'.encode())

PORT = 8088
print(f"🏛️ IMPERIAL SERVER STARTED on port {PORT}")
print(f"📡 Serving from: {os.getcwd()}")
print(f"🚚 Fleet data: http://localhost:{PORT}/fleet_data.json")
print(f"📊 Dashboard: http://localhost:{PORT}/")

with socketserver.TCPServer(("", PORT), ImperialRequestHandler) as httpd:
    httpd.serve_forever()
