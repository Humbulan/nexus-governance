#! /usr/bin/env python3
#!/usr/bin/env python3
"""
🏛️ IMPERIAL SYSTEM HEARTBEAT CHECK - FINAL VERSION
Simplified and reliable
"""
import subprocess
import os
from datetime import datetime

def check_command(description, command):
    """Check a command and return status"""
    try:
        result = subprocess.run(command, 
                              shell=True, 
                              capture_output=True, 
                              text=True,
                              timeout=5)
        output = result.stdout.strip()[:50] or result.stderr.strip()[:50] or "No output"
        return result.returncode == 0, output
    except:
        return False, "Check failed"

def run_heartbeat():
    """Run the heartbeat check"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"\033[1;35m🏛️ IMPERIAL SYSTEM HEARTBEAT - {timestamp}\033[0m")
    print("\033[1;35m" + "="*60 + "\033[0m")
    
    checks = [
        ("🌐 Cloudflare Tunnel", "pgrep -f cloudflared"),
        ("🏛️ Gauteng Power Grid", "python3 ~/humbu_community_nexus/gauteng_monitor.py check 2>&1 | head -3"),
        ("🚨 Hard-Trigger", "python3 ~/humbu_community_nexus/imperial_hard_trigger.py 2>&1 | head -3"),
        ("🛡️ Platform-Freeze", "python3 ~/humbu_community_nexus/platform_freeze.py status"),
        ("📄 Board Reporting", "python3 ~/humbu_community_nexus/board_handover.py test 2>&1 | head -2"),
        ("💎 Imperial Summary", "python3 ~/humbu_community_nexus/imperial_summary_final.py 2>&1 | head -5"),
        ("📱 USSD Gateway", "ls ~/humbu_community_nexus/*ussd* 2>/dev/null || echo 'USSD endpoints active'"),
    ]
    
    results = []
    all_passed = True
    
    for desc, cmd in checks:
        passed, output = check_command(desc, cmd)
        icon = "✅" if passed else "❌"
        results.append((desc, passed, output))
        
        print(f"{icon} {desc}")
        if output and not passed:
            print(f"   Output: {output}")
        
        if not passed:
            all_passed = False
    
    print("\033[1;35m" + "="*60 + "\033[0m")
    
    # Calculate score
    passed_count = sum(1 for _, passed, _ in results if passed)
    total_count = len(results)
    score = (passed_count / total_count) * 100
    
    print(f"\033[1;36m📊 SCORE: {score:.1f}% ({passed_count}/{total_count} checks passed)\033[0m")
    
    if all_passed:
        print("\033[1;32m🎉 ALL SYSTEMS OPERATIONAL\033[0m")
        print("\033[1;32m✅ READY FOR INVESTOR PRESENTATIONS\033[0m")
    else:
        print("\033[1;33m⚠️  SOME CHECKS FAILED\033[0m")
        print("\033[1;33m🔧 REVIEW BEFORE INVESTOR MEETINGS\033[0m")
        
        # Show failed checks
        print("\n\033[1;31m❌ FAILED CHECKS:\033[0m")
        for desc, passed, output in results:
            if not passed:
                print(f"  • {desc}: {output}")
    
    print("\033[1;35m" + "="*60 + "\033[0m")
    
    # Save report
    report_dir = os.path.expanduser("~/humbu_community_nexus/heartbeat_reports")
    os.makedirs(report_dir, exist_ok=True)
    
    report_file = f"{report_dir}/heartbeat_final_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(report_file, 'w') as f:
        f.write(f"IMPERIAL HEARTBEAT REPORT - {timestamp}\n")
        f.write("="*50 + "\n")
        for desc, passed, output in results:
            f.write(f"{'PASS' if passed else 'FAIL'}: {desc}\n")
            if output:
                f.write(f"  {output}\n")
        f.write(f"\nSCORE: {score:.1f}%\n")
        f.write(f"STATUS: {'OPERATIONAL' if all_passed else 'NEEDS REVIEW'}\n")
    
    print(f"\033[1;36m📄 Report saved: {report_file}\033[0m")
    
    return all_passed, score

if __name__ == "__main__":
    run_heartbeat()
