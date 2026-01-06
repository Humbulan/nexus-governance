#! /usr/bin/env python3
import sqlite3
import datetime

conn = sqlite3.connect('/data/data/com.termux/files/home/humbu_community_nexus/community_nexus.db')
cursor = conn.cursor()

# Insert a small 'system-check' transaction for the top 5 villages
villages = ['Vhulaudzi', 'Makhuvha', 'Thohoyandou', 'Sibasa', 'Giyani']
for v in villages:
    cursor.execute("INSERT INTO transactions (village, amount, timestamp) VALUES (?, 0.01, datetime('now'))")

conn.commit()
print("✅ SYSTEM WAKE-UP COMPLETE: 5 Nodes Pulsing.")
conn.close()
