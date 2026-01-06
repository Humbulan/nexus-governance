import shutil
import os
from datetime import datetime

def secure_backup():
    db_path = '/data/data/com.termux/files/home/humbu_community_nexus/community_nexus.db'
    vault_dir = '/data/data/com.termux/files/home/humbu_community_nexus/vault'
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    backup_name = f"IMPERIAL_BACKUP_{timestamp}.db"
    destination = os.path.join(vault_dir, backup_name)
    
    if os.path.exists(db_path):
        shutil.copy2(db_path, destination)
        print(f"🛡️ SHIELD ACTIVE: {backup_name} secured in vault.")
        
        # Keep only the last 5 backups to save space
        backups = sorted([f for f in os.listdir(vault_dir) if f.startswith('IMPERIAL_BACKUP')])
        if len(backups) > 5:
            os.remove(os.path.join(vault_dir, backups[0]))
            print("🧹 MAINTENANCE: Oldest backup rotated out.")
    else:
        print("❌ ERROR: Main Database not found!")

if __name__ == "__main__":
    secure_backup()
