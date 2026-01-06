import sqlite3
import datetime

def run_sage_audit():
    print("🧠 HUMBU IMPERIAL SAGE: SYSTEM INTELLIGENCE")
    print("============================================")
    
    conn = sqlite3.connect('/data/data/com.termux/files/home/humbu_community_nexus/community_nexus.db')
    cursor = conn.cursor()

    # 1. LATENCY CHECK
    print("🔍 AUDIT: Detecting Village Latency...")
    # Checking for any activity in the last 48 hours to account for the holiday
    cursor.execute("SELECT DISTINCT village FROM marketplace WHERE village NOT IN (SELECT village FROM transactions WHERE timestamp > datetime('now', '-2 days'))")
    silent_villages = cursor.fetchall()
    
    if len(silent_villages) > 20:
        print("ℹ️ HOLIDAY MODE: High latency detected across 50%+ of nodes. Monitoring only.")
    elif silent_villages:
        for v in silent_villages:
            print(f"⚠️ ALERT: {v[0]} is STAGNANT.")
    else:
        print("✅ LOGISTICS: All 40 villages showing active pulse.")

    # 2. REVENUE MOMENTUM
    weekly_rev = 6687.34 
    daily_avg = weekly_rev / 7
    projected_month = daily_avg * 30
    
    print(f"📈 MOMENTUM: R{daily_avg:.2f} avg/day")
    print(f"🔮 PREDICTION: Month-end yield R{projected_month:.2f}")
    
    # 3. GAUTENG READINESS INDEX
    # Readiness based on reaching a R10,000 weekly community volume threshold
    target_monthly = 416666.67
    readiness = (projected_month / target_monthly) * 100 
    print(f"🚀 GAUTENG READINESS: {min(readiness, 100):.1f}%")
    print(f"🏛️ ENPS ELIGIBILITY: {'QUALIFIED' if weekly_rev > 5000 else 'PENDING'}")
    
    print("============================================")
    conn.close()

if __name__ == "__main__":
    run_sage_audit()
