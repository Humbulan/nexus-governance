#! /usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class StatusHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/humbu_status.html'
        return SimpleHTTPRequestHandler.do_GET(self)
    
    def translate_path(self, path):
        # Serve from home directory
        return os.path.expanduser('~') + path

print("🚀 Starting Status Server on port 8081...")
print("🔗 Access at: http://localhost:8081/")
server = HTTPServer(('0.0.0.0', 8081), StatusHandler)
server.serve_forever()
