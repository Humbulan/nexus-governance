#!/data/data/com.termux/files/usr/bin/python3
import socket
import subprocess
from datetime import datetime

def check_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('localhost', port))
        sock.close()
        return result == 0
    except:
        return False

def check_cloudflare():
    try:
        # Check if cloudflared process is running
        result = subprocess.run(['pgrep', '-f', 'cloudflared'], 
                              capture_output=True, text=True)
        return len(result.stdout.strip()) > 0
    except:
        return False

print("📡 REAL-TIME SYSTEM STATUS")
print("==========================")
print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
print("")

# Check APIs
apis = [
    (9090, "Health API"),
    (8080, "Community Web"),
]

all_up = True
for port, name in apis:
    if check_port(port):
        print(f"✅ {name}: CONNECTED (port {port})")
    else:
        print(f"❌ {name}: DISCONNECTED")
        all_up = False

print("")

# Check Cloudflare
if check_cloudflare():
    print("🌐 CLOUDFLARE TUNNEL: CONNECTED (GREEN)")
    print("   Check ~/logs/cloudflared_ultra.log for URL")
else:
    print("🌐 CLOUDFLARE TUNNEL: DISCONNECTED (BLUE/RED)")
    print("   To fix: nohup cloudflared tunnel --url http://localhost:8080 > ~/logs/cloudflared.log 2>&1 &")

print("")
print("🔗 YOUR WORKING URLs:")
print("• http://localhost:8080/api/gauteng")
print("• http://localhost:8080/api/services")
print("• http://localhost:8080/api/transactions/latest")
print("• http://localhost:8080/api/revenue")
print("• http://localhost:9090/health")

if all_up:
    print("")
    print("🎉 SYSTEM STATUS: ALL OPERATIONAL")
else:
    print("")
    print("⚠️  SYSTEM STATUS: PARTIAL OUTAGE")
