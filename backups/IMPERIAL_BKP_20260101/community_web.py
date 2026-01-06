#!/data/data/com.termux/files/usr/bin/python3
"""
HUMBU COMMUNITY WEB PORTAL
Mobile-friendly interface for community members
"""

import http.server
import socketserver
import json
import os
import sqlite3
from pathlib import Path
from datetime import datetime

class CommunityHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP handler for community portal"""
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self.path = '/index.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/api/stats':
            self.send_stats()
        elif self.path == '/api/marketplace':
            self.send_marketplace()
        elif self.path == '/api/tasks':
            self.send_tasks()
        elif self.path == '/api/map':
            self.send_map_data()
        else:
            # Try to serve static files
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
    def send_stats(self):
        """Send community statistics as JSON"""
        db_path = Path.home() / "humbu_community_nexus" / "data" / "community.db"
        
        stats = {
            "platform": "Humbu Community Nexus",
            "region": "Thohoyandou & Surrounding Villages",
            "timestamp": datetime.now().isoformat(),
            "stats": {}
        }
        
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Get counts
            cursor.execute("SELECT COUNT(*) FROM users")
            stats["stats"]["total_users"] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM listings WHERE status = 'available'")
            stats["stats"]["market_listings"] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM tasks WHERE status = 'open'")
            stats["stats"]["open_tasks"] = cursor.fetchone()[0]
            
            cursor.execute("SELECT SUM(wallet_balance) FROM users")
            wallet_total = cursor.fetchone()[0] or 0
            stats["stats"]["total_wallet_value"] = wallet_total
            
            conn.close()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(stats).encode())
            
        except Exception as e:
            self.send_error(500, f"Database error: {str(e)}")
    
    def send_marketplace(self):
        """Send marketplace listings"""
        db_path = Path.home() / "humbu_community_nexus" / "data" / "community.db"
        
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
            SELECT l.item, l.price, l.quantity, l.unit, l.category, u.name, u.village
            FROM listings l
            JOIN users u ON l.user_id = u.id
            WHERE l.status = 'available'
            ORDER BY l.created_at DESC
            LIMIT 20
            """)
            
            listings = []
            for row in cursor.fetchall():
                listings.append({
                    "item": row[0],
                    "price": row[1],
                    "quantity": row[2],
                    "unit": row[3],
                    "category": row[4],
                    "seller": row[5],
                    "village": row[6]
                })
            
            conn.close()
            
            response = {
                "status": "success",
                "count": len(listings),
                "listings": listings
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            self.send_error(500, f"Database error: {str(e)}")
    
    def send_tasks(self):
        """Send available tasks"""
        db_path = Path.home() / "humbu_community_nexus" / "data" / "community.db"
        
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
            SELECT title, description, reward, duration_hours, category, 
                   datetime(created_at, 'localtime') as posted_time
            FROM tasks
            WHERE status = 'open'
            ORDER BY reward DESC
            LIMIT 15
            """)
            
            tasks = []
            for row in cursor.fetchall():
                tasks.append({
                    "title": row[0],
                    "description": row[1],
                    "reward": row[2],
                    "duration": row[3],
                    "category": row[4],
                    "posted": row[5]
                })
            
            conn.close()
            
            response = {
                "status": "success",
                "count": len(tasks),
                "tasks": tasks
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            self.send_error(500, f"Database error: {str(e)}")
    
    def send_map_data(self):
        """Send map data"""
        map_file = Path.home() / "humbu_community_nexus" / "community_map.json"
        
        try:
            with open(map_file, 'r') as f:
                map_data = json.load(f)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(map_data).encode())
            
        except Exception as e:
            self.send_error(500, f"Map file error: {str(e)}")

def run_server(port=8086):
    """Run the community web server"""
    print(f"🌐 Starting Community Web Portal on port {port}...")
    print(f"📱 Access: http://localhost:{port}")
    print("📍 Serving Thohoyandou & surrounding villages")
    
    os.chdir(Path.home() / "humbu_community_nexus")
    
    handler = CommunityHTTPRequestHandler
    
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"✅ Server running at http://localhost:{port}")
        print("🔄 Serving community data...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")

if __name__ == "__main__":
    run_server(8086)

# HUMBU LIVE MONITOR BRIDGE
@app.route('/api/monitor')
def live_monitor():
    import sqlite3
    conn = sqlite3.connect('community_nexus.db')
    cursor = conn.cursor()
    cursor.execute("SELECT amount, msisdn, timestamp FROM transactions WHERE status='SUCCESSFUL' ORDER BY timestamp DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"amount": row[0], "phone": row[1], "time": row[2]}
    return {"amount": 0}
