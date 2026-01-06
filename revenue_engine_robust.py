#! /usr/bin/env python3
#!/usr/bin/env python3
import socket
import time
import sys
import subprocess

def is_port_in_use(port):
    """Check if a port is in use"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('0.0.0.0', port))
            return False
        except OSError:
            return True

def find_available_port(start_port=8086):
    """Find an available port starting from start_port"""
    port = start_port
    while is_port_in_use(port):
        print(f"Port {port} in use, trying {port + 1}")
        port += 1
        if port > 8096:  # Don't go too high
            return None
    return port

# Try to start on available port
for attempt in range(3):
    port = find_available_port(8086 + attempt)
    if port:
        print(f"✅ Starting on port {port}")
        # Modify and run the original script
        with open("revenue_engine.py", "r") as f:
            content = f.read()
        content = content.replace("8086", str(port))
        
        with open(f"revenue_engine_port_{port}.py", "w") as f:
            f.write(content)
        
        # Run it
        subprocess.Popen([sys.executable, f"revenue_engine_port_{port}.py"])
        sys.exit(0)
    time.sleep(1)

print("❌ Could not find available port after 3 attempts")
sys.exit(1)
