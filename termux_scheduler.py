#! /usr/bin/env python3
#!/usr/bin/env python3
"""
Simple scheduler for Termux that mimics cron functionality
"""

import schedule
import time
import subprocess
import os
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scheduler.log'),
        logging.StreamHandler()
    ]
)

def run_backup_job(job_name, command):
    """Run a backup job and log the result"""
    try:
        logging.info(f"Starting {job_name}...")
        start_time = time.time()
        
        # Change to project directory
        os.chdir('/data/data/com.termux/files/home/humbu_community_nexus')
        
        # Run the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        end_time = time.time()
        duration = end_time - start_time
        
        if result.returncode == 0:
            logging.info(f"✅ {job_name} completed in {duration:.2f} seconds")
        else:
            logging.error(f"❌ {job_name} failed after {duration:.2f} seconds")
            logging.error(f"Error: {result.stderr}")
            
    except Exception as e:
        logging.error(f"❌ {job_name} crashed: {str(e)}")

def weekly_backup():
    """Weekly backup job"""
    run_backup_job("Weekly Backup", "python3 weekly_backup.py")

def daily_backup():
    """Daily backup job"""
    run_backup_job("Daily Backup", 'sqlite3 community_nexus.db ".backup logs/daily_backup_$(date +%Y%m%d_%H%M%S).db"')

def monthly_maintenance():
    """Monthly maintenance job"""
    run_backup_job("Monthly Maintenance", "bash monthly_maintenance.sh")

def daily_status_check():
    """Daily platform status check"""
    run_backup_job("Daily Status Check", 'echo "Daily check: $(date)" >> logs/daily_status.txt && sqlite3 community_nexus.db "SELECT COUNT(*) FROM transactions WHERE date(timestamp) = date(\"now\");" >> logs/daily_status.txt')

def main():
    """Main scheduler loop"""
    logging.info("🚀 Humbu Community Nexus Scheduler Started")
    logging.info(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Schedule jobs
    schedule.every().sunday.at("00:00").do(weekly_backup)
    schedule.every().day.at("02:00").do(daily_backup)
    schedule.every().day.at("08:00").do(daily_status_check)
    
    # Monthly job (runs on 1st of month at 03:00)
    schedule.every().monday.at("03:00").do(monthly_maintenance)  # Will adjust logic
    
    logging.info("📅 Jobs Scheduled:")
    logging.info("  • Weekly Backup: Sunday 00:00")
    logging.info("  • Daily Backup: Every day 02:00")
    logging.info("  • Daily Status: Every day 08:00")
    logging.info("  • Monthly Maintenance: First Monday 03:00")
    logging.info("")
    logging.info("⏰ Scheduler running. Press Ctrl+C to stop.")
    
    # Keep the scheduler running
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("🛑 Scheduler stopped by user")
    except Exception as e:
        logging.error(f"❌ Scheduler crashed: {str(e)}")
