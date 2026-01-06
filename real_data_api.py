#! /usr/bin/env python3
from flask import Flask, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/api/real/revenue')
def real_revenue():
    conn = sqlite3.connect('community_nexus.db')
    cursor = conn.cursor()
    
    # Get actual revenue data
    cursor.execute("SELECT SUM(amount) FROM transactions")
    total_revenue = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT COUNT(*) FROM transactions WHERE date(timestamp) = date('now')")
    today_transactions = cursor.fetchone()[0]
    
    conn.close()
    
    return jsonify({
        "total_revenue": f"R{total_revenue:.2f}",
        "today_transactions": today_transactions,
        "projected_monthly": f"R{total_revenue * 30:.2f}",
        "last_updated": datetime.now().strftime("%H:%M:%S")
    })

if __name__ == '__main__':
    app.run(port=8090)
