#!/bin/bash

echo "🔒 HUMBU COMMUNITY NEXUS - MONTHLY MAINTENANCE"
echo "=============================================="
echo "Date: $(date)"
echo ""

# Create backup directory if it doesn't exist
BACKUP_DIR="database_backups"
mkdir -p "$BACKUP_DIR"

# Generate backup filename with timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/community_nexus_backup_$TIMESTAMP.db"

# 1. Backup the database
echo "📦 BACKING UP DATABASE..."
cp community_nexus.db "$BACKUP_FILE"
echo "✅ Database backed up to: $BACKUP_FILE"

# 2. Create SQL dump for safety
echo "💾 CREATING SQL DUMP..."
SQL_DUMP="$BACKUP_DIR/community_nexus_dump_$TIMESTAMP.sql"
sqlite3 community_nexus.db .dump > "$SQL_DUMP"
echo "✅ SQL dump created: $SQL_DUMP"

# 3. Create JSON backup of transactions
echo "📊 BACKING UP TRANSACTIONS..."
python3 -c "
import sqlite3, json
db = sqlite3.connect('community_nexus.db')
cursor = db.cursor()

# Get transactions
cursor.execute('SELECT * FROM transactions')
transactions = cursor.fetchall()

# Get column names
cursor.execute('PRAGMA table_info(transactions)')
columns = [col[1] for col in cursor.fetchall()]

# Convert to list of dictionaries
tx_list = []
for tx in transactions:
    tx_dict = {}
    for i, col in enumerate(columns):
        tx_dict[col] = tx[i]
    tx_list.append(tx_dict)

# Save to JSON
with open('$BACKUP_DIR/transactions_backup_$TIMESTAMP.json', 'w') as f:
    json.dump(tx_list, f, indent=2)

print(f'   Backed up {len(tx_list)} transactions')

db.close()
"

# 4. Create marketplace backup
echo "🏪 BACKING UP MARKETPLACE..."
python3 -c "
import sqlite3, json, csv
db = sqlite3.connect('community_nexus.db')
cursor = db.cursor()

# Get marketplace data
cursor.execute('SELECT * FROM marketplace')
marketplace = cursor.fetchall()

# Get column names
cursor.execute('PRAGMA table_info(marketplace)')
columns = [col[1] for col in cursor.fetchall()]

# Save as CSV (easier to read)
with open('$BACKUP_DIR/marketplace_backup_$TIMESTAMP.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    writer.writerows(marketplace)

print(f'   Backed up {len(marketplace)} marketplace items')

db.close()
"

# 5. Clean old backups (keep last 30 days)
echo "🧹 CLEANING OLD BACKUPS..."
find "$BACKUP_DIR" -name "*.db" -mtime +30 -delete
find "$BACKUP_DIR" -name "*.sql" -mtime +30 -delete
find "$BACKUP_DIR" -name "*.json" -mtime +30 -delete
find "$BACKUP_DIR" -name "*.csv" -mtime +30 -delete
echo "✅ Old backups cleaned (keeping last 30 days)"

# 6. Database optimization
echo "⚡ OPTIMIZING DATABASE..."
sqlite3 community_nexus.db "VACUUM;"
sqlite3 community_nexus.db "ANALYZE;"
echo "✅ Database optimized"

# 7. Create maintenance report
echo "📋 GENERATING MAINTENANCE REPORT..."
python3 -c "
from datetime import datetime
import os, json

report = {
    'maintenance_date': datetime.now().isoformat(),
    'backup_files': [],
    'statistics': {}
}

# List backup files
for file in os.listdir('$BACKUP_DIR'):
    if file.endswith(('.db', '.sql', '.json', '.csv')):
        path = os.path.join('$BACKUP_DIR', file)
        size = os.path.getsize(path)
        report['backup_files'].append({
            'filename': file,
            'size_bytes': size,
            'size_mb': round(size / (1024 * 1024), 2)
        })

# Get database statistics
import sqlite3
db = sqlite3.connect('community_nexus.db')
cursor = db.cursor()

cursor.execute('SELECT COUNT(*) FROM marketplace')
report['statistics']['marketplace_items'] = cursor.fetchone()[0]

cursor.execute('SELECT COUNT(*) FROM transactions')
report['statistics']['transactions'] = cursor.fetchone()[0]

cursor.execute('SELECT COUNT(DISTINCT village) FROM marketplace')
report['statistics']['villages_covered'] = cursor.fetchone()[0]

db.close()

# Save report
with open('$BACKUP_DIR/maintenance_report_$TIMESTAMP.json', 'w') as f:
    json.dump(report, f, indent=2)

print(f'   Report generated with {len(report[\"backup_files\"])} backup files')
"

echo ""
echo "🎯 MAINTENANCE COMPLETE!"
echo "📁 All backups saved in: $BACKUP_DIR/"
echo "🔒 Community ledger is SAFE"
echo "📅 Next maintenance: $(date -d '+30 days' '+%Y-%m-%d')"
echo ""
echo "✅ HUMBU COMMUNITY NEXUS IS SECURE AND READY!"
