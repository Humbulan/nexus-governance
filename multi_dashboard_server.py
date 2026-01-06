#! /usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import urllib.parse

class MultiDashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the path
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        # Map URLs to dashboard files
        dashboard_map = {
            '/': 'tunnel-dashboard.html',
            '/tunnel': 'tunnel-dashboard.html',
            '/portal': 'dashboard_index_fixed.html',
            '/navigation': 'navigation-hub.html',
            '/master': 'master_portal.html',
            '/community': 'dashboard_index.html',
            '/live': 'live-map.html',
            '/map': 'opportunity_map_visual.html',
            '/qr': 'qr_gallery.html',
            '/test': 'test_access.html',
            '/fixed': 'fixed-dashbox.html',
            '/cluster': 'tunnel-cluster.html'
        }
        
        # Check if this is a dashboard request
        if path in dashboard_map:
            file_to_serve = dashboard_map[path]
            if os.path.exists(file_to_serve):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                with open(file_to_serve, 'rb') as f:
                    self.wfile.write(f.read())
                return
        
        # Default: serve the requested file or directory listing
        super().do_GET()
    
    def list_directory(self, path):
        # Custom directory listing with dashboard links
        try:
            list = os.listdir(path)
        except OSError:
            self.send_error(404, "No permission to list directory")
            return None
        
        list.sort(key=lambda a: a.lower())
        r = []
        displaypath = urllib.parse.unquote(self.path, errors='surrogatepass')
        
        # Header with dashboard links
        html = f'''<!DOCTYPE HTML>
<html lang="en">
<head>
<meta charset="utf-8">
<title>🏛️ Humbu Imperial - Dashboard Hub</title>
<style>
    body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
    .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
    h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
    .dashboard-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; margin: 20px 0; }}
    .dashboard-card {{ background: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #3498db; }}
    .dashboard-card h3 {{ margin-top: 0; color: #2c3e50; }}
    .btn {{ display: inline-block; padding: 8px 16px; background: #3498db; color: white; text-decoration: none; border-radius: 4px; margin-top: 10px; }}
    .btn:hover {{ background: #2980b9; }}
</style>
</head>
<body>
<div class="container">
    <h1>🏛️ Humbu Imperial - Dashboard Hub</h1>
    <p>Port: 8082 | Serving all dashboards from one location</p>
    
    <div class="dashboard-grid">
        <div class="dashboard-card">
            <h3>🌐 Tunnel Dashboard</h3>
            <p>Cloudflare tunnel status and system overview</p>
            <a href="/tunnel" class="btn">Open</a>
        </div>
        
        <div class="dashboard-card">
            <h3>🏛️ Imperial Portal</h3>
            <p>Main dashboard with all system links</p>
            <a href="/portal" class="btn">Open</a>
        </div>
        
        <div class="dashboard-card">
            <h3>🧭 Navigation Hub</h3>
            <p>Quick navigation to all services</p>
            <a href="/navigation" class="btn">Open</a>
        </div>
        
        <div class="dashboard-card">
            <h3>👑 Master Portal</h3>
            <p>Complete system control panel</p>
            <a href="/master" class="btn">Open</a>
        </div>
        
        <div class="dashboard-card">
            <h3>🗺️ Live Map</h3>
            <p>Real-time opportunity visualization</p>
            <a href="/live" class="btn">Open</a>
        </div>
        
        <div class="dashboard-card">
            <h3>📱 QR Gallery</h3>
            <p>QR code gallery for deployments</p>
            <a href="/qr" class="btn">Open</a>
        </div>
    </div>
    
    <h2>📁 File Listing: {displaypath}</h2>
    <ul>
'''
        
        for name in list:
            fullname = os.path.join(path, name)
            displayname = name
            if os.path.isdir(fullname):
                displayname = name + "/"
            html += f'        <li><a href="{urllib.parse.quote(displayname, errors="surrogatepass")}">{displayname}</a></li>\n'
        
        html += '''    </ul>
</div>
</body>
</html>'''
        
        encoded = html.encode('utf-8', 'surrogateescape')
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

def run_server():
    os.chdir(os.path.expanduser('~/humbu_community_nexus'))
    server = HTTPServer(('localhost', 8082), MultiDashboardHandler)
    print("🚀 Multi-Dashboard Server running on http://localhost:8082")
    print("   Available dashboards:")
    print("   • /tunnel     - Tunnel dashboard")
    print("   • /portal     - Imperial portal")
    print("   • /navigation - Navigation hub")
    print("   • /master     - Master portal")
    print("   • /live       - Live map")
    print("   • /qr         - QR gallery")
    print("   • /           - Dashboard hub")
    server.serve_forever()

if __name__ == '__main__':
    run_server()
