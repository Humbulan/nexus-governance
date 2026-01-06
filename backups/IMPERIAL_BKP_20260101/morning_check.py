import os
import time

def run_health_check():
    print("\n🌅 GOOD MORNING, HUMBULANI.")
    print("⏳ Running Humbu Nexus System Health Check...")
    time.sleep(1)

    checks = {
        "User Database": os.path.exists("data/community.db"),
        "MoMo Module": os.path.exists("mobile_money/mtn_momo_real.py"),
        "Transaction Logs": os.path.exists("data/user_registry.csv"),
    }

    print("\n🛡️ SYSTEM INTEGRITY:")
    for component, status in checks.items():
        icon = "✅" if status else "❌"
        print(f"   {icon} {component}")

    print("\n📢 REMINDER:")
    print("   Target: 308 Users (Currently 208)")
    print("   Priority: Email MTN for Production Keys!")
    print("==========================================\n")

if __name__ == "__main__":
    run_health_check()
