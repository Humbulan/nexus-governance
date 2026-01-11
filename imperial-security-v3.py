import http.server
import socketserver
import os

PORT = 8082
DASHBOARD = "imperial-dashboard-8082.html"

class SovereignHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"🔒 SECURITY CHECK: {self.path}")
        
        # PROTECT THE CORE: Only allow these specific paths
        allowed = [
            '/' + DASHBOARD,
            '/village_data.json',
            '/IDC_SOVEREIGN_AUDIT.txt',
            '/source_proof',
            '/favicon.ico'
        ]
        
        # Allow source proof directory and its contents
        if self.path.startswith('/source_proof/'):
            if os.path.exists('.' + self.path):
                return super().do_GET()
            else:
                self.send_404()
                return
        
        # Root redirect to dashboard
        if self.path == '/' or self.path == '/index.html':
            print(f"📍 Redirecting root to {DASHBOARD}")
            self.send_response(301)
            self.send_header('Location', '/' + DASHBOARD)
            self.end_headers()
            return
        
        # Check if path is explicitly allowed
        if self.path in allowed:
            print(f"✅ Allowed: {self.path}")
            return super().do_GET()
        
        # BLOCK EVERYTHING ELSE WITH 403
        print(f"🚫 Blocked: {self.path}")
        self.send_response(403)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f'''
        <html>
        <body style="background: #0a1929; color: #ff4444; font-family: monospace; padding: 40px;">
            <h1>🚫 403: ACCESS DENIED</h1>
            <h2>Humbu Imperial Security Protocol V3</h2>
            <hr>
            <p><strong>Blocked Path:</strong> {self.path}</p>
            <p><strong>Reason:</strong> Legacy/unauthorized endpoint</p>
            <p><strong>Time:</strong> {self.date_time_string()}</p>
            <hr>
            <h3>✅ Authorized Endpoints:</h3>
            <ul>
                <li><a href="/imperial-dashboard-8082.html" style="color: #00ff88;">Imperial Dashboard</a></li>
                <li><a href="/village_data.json" style="color: #00aaff;">Village Data (JSON)</a></li>
                <li><a href="/IDC_SOVEREIGN_AUDIT.txt" style="color: #ffaa00;">Financial Audit</a></li>
                <li><a href="/source_proof" style="color: #00aaff;">Source Proof</a></li>
            </ul>
            <hr>
            <p><strong>CEO:</strong> Humbulani Mudau</p>
            <p><strong>Portfolio:</strong> R9,327,935.17</p>
            <p><strong>Status:</strong> 🔒 SECURE</p>
        </body>
        </html>
        '''.encode())
    
    def send_404(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>404: Not Found</h1><p>File does not exist in sovereign territory.</p>")
    
    def log_message(self, format, *args):
        # Only log security events
        message = format % args
        if "403" in message or "301" in message:
            print(f"🛡️ {message}")

print(f"🏛️ IMPERIAL GATEKEEPER V3 ACTIVATED")
print(f"📍 Port: {PORT}")
print(f"✅ Allowed:")
print(f"   • /imperial-dashboard-8082.html")
print(f"   • /village_data.json")
print(f"   • /IDC_SOVEREIGN_AUDIT.txt")
print(f"   • /source_proof/*")
print(f"🚫 Blocked: Everything else")
print(f"🔄 Root redirect: → /imperial-dashboard-8082.html")
print(f"🔒 Security: 403 Forbidden on all unauthorized access")

with socketserver.TCPServer(("", PORT), SovereignHandler) as httpd:
    httpd.serve_forever()
