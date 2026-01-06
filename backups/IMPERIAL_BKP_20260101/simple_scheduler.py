#!/usr/bin/env python3
import time
import subprocess
import os
from datetime import datetime
import schedule

# --- CONFIGURATION ---
# Replace with your actual number on the other device
MY_MAIN_NUMBER = "27xxxxxxxxx" 

def log_message(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_line = f"[{timestamp}] {message}"
    print(log_line)
    with open('scheduler.log', 'a') as f:
        f.write(log_line + '\n')

def run_job(command, job_name):
    try:
        log_message(f"Starting {job_name}...")
        os.chdir('/data/data/com.termux/files/home/humbu_community_nexus')
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            log_message(f"✅ {job_name} completed")
        else:
            log_message(f"❌ {job_name} failed")
    except Exception as e:
        log_message(f"❌ {job_name} crashed: {str(e)}")

def main():
    log_message("🚀 Humbu Nexus Scheduler Started")

    # 1. Daily Backups at 02:00
    schedule.every().day.at("02:00").do(lambda: run_job("sqlite3 community_nexus.db \".backup logs/daily.db\"", "Daily Backup"))
    
    # 2. Daily Status Check at 08:00
    schedule.every().day.at("08:00").do(lambda: run_job("python3 daily_status_check.py", "Daily Status Check"))
    
    # 3. YOUR PAYOUT SMS: Every Friday at 16:30
    schedule.every().friday.at("16:30").do(lambda: run_job("python3 weekly_sms_payout.py", "Weekly SMS Payout"))

    log_message("📅 All jobs scheduled. SMS report set for Fridays 16:30.")

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()

# Add this function to simple_scheduler.py
def weekly_payout():
    """Run weekly payout summary"""
    run_job("python3 weekly_payout.py", "Weekly Payout")
    
# And schedule it (add to main() function):
schedule.every().sunday.at("18:00").do(weekly_payout)
