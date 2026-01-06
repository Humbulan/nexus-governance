import os
import subprocess
import getpass
import sys

def run_command(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode('utf-8')
    except:
        return "OFFLINE"

# --- SECURITY GATE ---
PIN = "2026"
print("\033[1;31m[!] SECURITY CHALLENGE: HUMBU IMPERIAL ACCESS\033[0m")
attempt = getpass.getpass("ENTER CUSTODIAN PIN: ")

if attempt != PIN:
    print("\033[1;31m[X] ACCESS DENIED\033[0m")
    sys.exit()

print("\n\033[1;33m🏛️ HUMBU IMPERIAL CONSOLE v4.1 - YEAR 2026 READY\033[0m")
print("==================================================")

# 1. TUNNEL GUARD CHECK
tunnel_status = run_command("pgrep cloudflared")
if tunnel_status != "OFFLINE":
    print("\033[1;32m📡 CLOUDFLARE TUNNEL: ACTIVE (PIDs: " + tunnel_status.strip().replace('\n', ', ') + ")\033[0m")
else:
    print("\033[1;31m📡 CLOUDFLARE TUNNEL: DISCONNECTED\033[0m")

# 2. RUN SAGE INTELLIGENCE
print(run_command("python3 ~/humbu_community_nexus/imperial_sage.py"))

# 3. RUN VILLAGE LEADERBOARD
print(run_command("python3 ~/humbu_community_nexus/village_leaderboard.py"))
print(run_command("python3 ~/humbu_community_nexus/gauteng_monitor.py"))

# 4. SHOW GAUTENG STATUS
print("\033[1;36m🌐 EXPANSION NODE: GAUTENG\033[0m")
print("Status: INITIALIZED | Target: R5,000,000.00")
print("==================================================")
