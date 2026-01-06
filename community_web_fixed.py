#! /usr/bin/env python3
#!/usr/bin/env python3
import http.server
import socketserver
import json
import os
from datetime import datetime
import argparse

class CommunityRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html_content = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Humbu Community Nexus - Imperial Dashboard</title>
                <style>
                    body { 
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                        margin: 0; 
                        padding: 20px; 
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white;
                        min-height: 100vh;
                    }
                    .container { 
                        max-width: 1200px; 
                        margin: 0 auto; 
                        background: rgba(255, 255, 255, 0.1);
                        backdrop-filter: blur(10px);
                        border-radius: 20px;
                        padding: 30px;
                        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                    }
                    header { 
                        text-align: center; 
                        margin-bottom: 40px; 
                        padding-bottom: 20px;
                        border-bottom: 2px solid rgba(255,255,255,0.2);
                    }
                    h1 { 
                        font-size: 2.8em; 
                        margin-bottom: 10px;
                        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                    }
                    .tagline {
                        font-size: 1.2em;
                        opacity: 0.9;
                        margin-bottom: 30px;
                    }
                    .grid { 
                        display: grid; 
                        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
                        gap: 25px; 
                        margin-bottom: 40px;
                    }
                    .card { 
                        background: rgba(255, 255, 255, 0.15);
                        border-radius: 15px;
                        padding: 25px;
                        transition: transform 0.3s, background 0.3s;
                        border: 1px solid rgba(255,255,255,0.1);
                    }
                    .card:hover {
                        transform: translateY(-5px);
                        background: rgba(255, 255, 255, 0.25);
                    }
                    .card h2 { 
                        margin-top: 0; 
                        color: #fff;
                        font-size: 1.5em;
                        border-bottom: 2px solid rgba(255,255,255,0.3);
                        padding-bottom: 10px;
                    }
                    .status-badge {
                        display: inline-block;
                        padding: 5px 15px;
                        border-radius: 20px;
                        font-weight: bold;
                        margin-bottom: 15px;
                    }
                    .status-active { background: #10b981; }
                    .status-warning { background: #f59e0b; }
                    .status-critical { background: #ef4444; }
                    .data-value {
                        font-size: 1.8em;
                        font-weight: bold;
                        margin: 10px 0;
                    }
                    .cta-button {
                        display: inline-block;
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white;
                        padding: 12px 25px;
                        border-radius: 10px;
                        text-decoration: none;
                        font-weight: bold;
                        margin-top: 15px;
                        border: 2px solid rgba(255,255,255,0.3);
                        transition: all 0.3s;
                    }
                    .cta-button:hover {
                        transform: scale(1.05);
                        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
                    }
                    .imperial-banner {
                        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
                        padding: 15px;
                        border-radius: 10px;
                        text-align: center;
                        margin-bottom: 30px;
                        font-weight: bold;
                        font-size: 1.1em;
                    }
                    footer {
                        text-align: center;
                        margin-top: 40px;
                        padding-top: 20px;
                        border-top: 1px solid rgba(255,255,255,0.2);
                        font-size: 0.9em;
                        opacity: 0.8;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <header>
                        <h1>🏛️ HUMBU COMMUNITY NEXUS</h1>
                        <div class="tagline">Imperial Stack - Thohoyandou Command Center</div>
                        <div class="imperial-banner">
                            🚀 IDC PRESENTATION READY | SAGE AI: R9M APRIL 2026 FORECAST ACTIVE
                        </div>
                    </header>
                    
                    <div class="grid">
                        <div class="card">
                            <div class="status-badge status-active">🟢 OPERATIONAL</div>
                            <h2>💰 FINANCIAL COMMAND</h2>
                            <div class="data-value">R595,238.10</div>
                            <p>Monthly Revenue Capacity</p>
                            <a href="http://localhost:8088/index_financial_command.html" class="cta-button">Access Financial Dashboard</a>
                        </div>
                        
                        <div class="card">
                            <div class="status-badge status-active">🟢 OPERATIONAL</div>
                            <h2>🧠 SAGE INTELLIGENCE</h2>
                            <div class="data-value">R9,084,769</div>
                            <p>April 2026 Projection (438.9% Growth)</p>
                            <a href="http://localhost:8088" class="cta-button">View AI Predictions</a>
                        </div>
                        
                        <div class="card">
                            <div class="status-badge status-active">🟢 OPERATIONAL</div>
                            <h2>🏭 INDUSTRIAL GRID</h2>
                            <div class="data-value">R412,730.15</div>
                            <p>Verified Industrial Backing</p>
                            <a href="http://localhost:8088/index_financial_command.html#industrial" class="cta-button">View Industrial Data</a>
                        </div>
                    </div>
                    
                    <div class="grid">
                        <div class="card">
                            <h2>🌐 ACCESS POINTS</h2>
                            <p><strong>Executive Dashboard:</strong><br>http://localhost:8088</p>
                            <p><strong>Public Portal:</strong><br>monitor.humbu.store</p>
                            <p><strong>Automation:</strong><br>http://localhost:1880</p>
                            <a href="http://localhost:8088" class="cta-button">Launch All Portals</a>
                        </div>
                        
                        <div class="card">
                            <h2>🛡️ RECOVERY PROTOCOL</h2>
                            <p>System Revival Command:</p>
                            <code style="background: rgba(0,0,0,0.3); padding: 10px; border-radius: 5px; display: block; margin: 10px 0;">
                                nexus-revive
                            </code>
                            <p>Instant recovery of all Imperial Stack components</p>
                        </div>
                        
                        <div class="card">
                            <h2>📊 IDC BRIEFING</h2>
                            <p><strong>Enquiry:</strong> #4000120009 (SENTC)</p>
                            <p><strong>R5M Milestone:</strong> March 2026 (99.8%)</p>
                            <p><strong>Current Progress:</strong> 11.9% (R595k/mo)</p>
                            <a href="#" class="cta-button">Download Briefing Package</a>
                        </div>
                    </div>
                    
                    <footer>
                        <p>Humbu Community Nexus | Imperial Stack v2.0</p>
                        <p>📍 Serving Thohoyandou & Surrounding Villages | 🏛️ IDC Ready</p>
                        <p>© 2026 Humbu Empire | All Systems Operational</p>
                    </footer>
                </div>
            </body>
            </html>
            '''
            self.wfile.write(html_content.encode())
        else:
            super().do_GET()

def run_server(port=8086):
    print(f"🌐 Starting Community Web Portal on port {port}...")
    print(f"📱 Access: http://localhost:{port}")
    print("📍 Serving Thohoyandou & surrounding villages")
    print("🏛️ Imperial Stack: 100% Operational | IDC Presentation Ready")
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    handler = CommunityRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"✅ Server running on port {port}")
        print("🛑 Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Humbu Community Nexus Web Portal')
    parser.add_argument('--port', type=int, default=8086, help='Port to run server on')
    args = parser.parse_args()
    
    run_server(args.port)
