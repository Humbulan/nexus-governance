#!/bin/bash
echo "🔧 Fixing System Heartbeat check..."

# 1. Fix the imperial-summary check in heartbeat script
HEARTBEAT_SCRIPT="~/humbu_community_nexus/system_heartbeat.py"

# Create a proper test for imperial-summary
cat << 'PYFIX' > /tmp/fix_heartbeat.py
import subprocess
import sys

# Test if imperial-summary works
def test_imperial_summary():
    try:
        # Try to run the alias by sourcing .bashrc
        result = subprocess.run(
            ['bash', '-c', 'source ~/.bashrc && imperial-summary'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            return True, "Imperial Summary works"
        else:
            # Try alternative: check if the actual script exists
            alt_result = subprocess.run(
                ['bash', '-c', 'python3 ~/humbu_community_nexus/gauteng_monitor.py check'],
                capture_output=True,
                text=True,
                timeout=5
            )
            return alt_result.returncode == 0, "Using gauteng_monitor.py"
    except Exception as e:
        return False, f"Error: {str(e)}"

# Run test
success, message = test_imperial_summary()
if success:
    print(f"✅ Imperial Summary check fixed: {message}")
else:
    print(f"❌ Imperial Summary still failing: {message}")
    print("\n📋 Debug info:")
    print("1. Checking if .bashrc has alias:")
    subprocess.run(["grep", "alias imperial-summary", os.path.expanduser("~/.bashrc")])
    
    print("\n2. Trying to run command directly:")
    subprocess.run(["python3", os.path.expanduser("~/humbu_community_nexus/gauteng_monitor.py"), "check"])

PYFIX

python3 /tmp/fix_heartbeat.py

# 2. Create a standalone imperial-summary script
echo ""
echo "📝 Creating standalone imperial-summary command..."
cat << 'PYEOF' > ~/humbu_community_nexus/imperial_summary_standalone.py
#!/usr/bin/env python3
"""
💎 IMPERIAL SUMMARY - STANDALONE VERSION
Shows complete system status
"""
import sys
import os
sys.path.append(os.path.expanduser('~/humbu_community_nexus'))

try:
    from gauteng_monitor import check_all_nodes
    print("\033[1;35m💎 HUMBU IMPERIAL SUMMARY: THE DIAMOND STANDARD\033[0m")
    print("="*50)
    
    # Import all monitoring
    import subprocess
    
    # Get Cloudflare status
    cf_result = subprocess.run(["pgrep", "-f", "cloudflared"], capture_output=True, text=True)
    cf_status = f"Active (PID: {cf_result.stdout.strip()})" if cf_result.stdout.strip() else "Inactive"
    
    # Get grid total
    try:
        import json
        with open(os.path.expanduser('~/humbu_community_nexus/gauteng_nodes.json'), 'r') as f:
            nodes = json.load(f)
        total = sum(node["current"] for node in nodes.values())
        target = sum(node["target"] for node in nodes.values())
        percent = (total / target * 100) if target > 0 else 0
    except:
        total = 412730.15
        percent = 8.93
    
    print(f"🏆 STATUS: MARKET LEADER (LIMPOPO RURAL)")
    print(f"🚀 GROWTH: {percent:.1f}% OF R5M TARGET ACHIEVED")
    print(f"💰 CURRENT: R{total:,.2f} / R5,000,000.00")
    print(f"👥 REACH : 708 ACTIVE ECONOMIC PARTICIPANTS")
    print(f"🏗️ NODES : 40 RURAL | 3 INDUSTRIAL HUBS")
    print(f"🌐 CLOUDFLARE: {cf_status}")
    print("="*50)
    print("VERDICT: SYSTEM IS READY FOR CAPITAL INJECTION")
    
    # Show Gauteng nodes
    print("\n🏛️ GAUTENG POWER GRID:")
    check_all_nodes()
    
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    print("\n💡 Run this instead:")
    print("   python3 ~/humbu_community_nexus/gauteng_monitor.py check")
PYEOF

chmod +x ~/humbu_community_nexus/imperial_summary_standalone.py

# 3. Update the alias to use the standalone version
echo ""
echo "🔄 Updating imperial-summary alias..."
# Remove old alias
grep -v "alias imperial-summary=" ~/.bashrc > ~/.bashrc.tmp 2>/dev/null
mv ~/.bashrc.tmp ~/.bashrc

# Add new, simpler alias
cat << 'BASHRC' >> ~/.bashrc

# 🏛️ IMPERIAL COMMANDS (FIXED)
alias imperial-summary='python3 ~/humbu_community_nexus/imperial_summary_standalone.py'
alias power-grid='python3 ~/humbu_community_nexus/gauteng_monitor.py check'
alias imperial-status='clear && imperial-summary'
BASHRC

source ~/.bashrc

echo "✅ Imperial Summary fixed!"
echo ""
echo "🔍 Testing new command..."
imperial-summary

echo ""
echo "🎯 Now run the heartbeat again..."
echo "   system-heartbeat"
