#! /usr/bin/env python3
import os

header = """<!DOCTYPE html><html><head><title>Humbu Imperial Logistics</title>
<style>body{background:#0a0a12;color:white;font-family:sans-serif;}
table{width:100%;border-collapse:collapse;} th{background:#1e3a8a;padding:10px;}
td{padding:8px;border-bottom:1px solid #1e293b;}</style></head>
<body><h1>🏛️ HUMBU IMPERIAL LOGISTICS COMMAND</h1><table>
<tr><th>Vehicle ID</th><th>Status</th><th>Location</th><th>Temp</th></tr>"""

footer = "</table></body></html>"

# Replace this with your actual data file path
with open('index.html', 'w') as f:
    f.write(header + "" + footer)
