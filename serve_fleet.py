#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import time
import os

class FleetHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/fleet_telemetry.json':
            # Update timestamp
            with open('fleet_telemetry.json', 'r') as f:
                data = json.load(f)
            
            # Force new data (avoid 304)
            data['last_update'] = time.strftime('%Y-%m-%dT%H:%M:%S.%fZ', time.gmtime())
            data['timestamp'] = int(time.time())
            data['metrics']['last_system_update'] = time.strftime('%H:%M:%S')
            
            # Send fresh response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            self.send_header('Last-Modified', time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime()))
            self.end_headers()
            
            self.wfile.write(json.dumps(data).encode())
        else:
            # Serve normal files
            super().do_GET()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer(('localhost', 8088), FleetHandler)
    print('🚚 Fleet Telemetry Server running on http://localhost:8088')
    print('📡 Fleet data: http://localhost:8088/fleet_telemetry.json')
    server.serve_forever()
