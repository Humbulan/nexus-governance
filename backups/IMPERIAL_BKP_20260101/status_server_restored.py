from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class StatusHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/humbu_status.html'
        return SimpleHTTPRequestHandler.do_GET(self)
    
    def translate_path(self, path):
        return os.path.expanduser('~') + path

print("🚀 Status Server restored on port 8081...")
print("🔗 Access at: http://localhost:8081/")
server = HTTPServer(('0.0.0.0', 8081), StatusHandler)
server.serve_forever()
