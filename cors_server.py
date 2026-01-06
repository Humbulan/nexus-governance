import http.server
import socketserver

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

PORT = 8088
with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    print("🚀 Imperial Dashboard Live on Port", PORT)
    httpd.serve_forever()
