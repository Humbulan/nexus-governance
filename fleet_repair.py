#! /usr/bin/env python3
import os

table_data = """
<tr><td>HMB-FLEET-01</td><td><span class='status returning'>Returning</span></td><td>SADC Border Link</td><td>3.4°C</td><td>Live</td></tr>
<tr><td>HMB-FLEET-02</td><td><span class='status intransit'>In Transit</span></td><td>Thohoyandou-F</td><td>4.0°C</td><td>Live</td></tr>
<tr><td>HMB-FLEET-03</td><td><span class='status unloading'>Unloading</span></td><td>Gauteng Gateway</td><td>2.4°C</td><td>Live</td></tr>
<tr><td>HMB-FLEET-04</td><td><span class='status returning'>Returning</span></td><td>Gauteng Gateway</td><td>3.0°C</td><td>Live</td></tr>
<tr><td>HMB-FLEET-05</td><td><span class='status intransit'>In Transit</span></td><td>Gauteng Gateway</td><td>3.0°C</td><td>Live</td></tr>
<tr><td>HMB-FLEET-06</td><td><span class='status intransit'>In Transit</span></td><td>Gauteng Gateway</td><td>3.2°C</td><td>Live</td></tr>
<tr><td>HMB-FLEET-07</td><td><span class='status loading'>Loading</span></td><td>Manilini South</td><td>2.9°C</td><td>Live</td></tr>
<tr><td>HMB-FLEET-08</td><td><span class='status intransit'>In Transit</span></td><td>Thohoyandou-F</td><td>4.3°C</td><td>Live</td></tr>
<tr><td>HMB-FLEET-09</td><td><span class='status returning'>Returning</span></td><td>Vhembe District Hub</td><td>2.5°C</td><td>Live</td></tr>
<tr><td>HMB-FLEET-10</td><td><span class='status optimizing'>Optimizing</span></td><td>Manilini South</td><td>4.9°C</td><td>Live</td></tr>
"""

with open('/data/data/com.termux/files/home/humbu_community_nexus/index.html', 'r') as f:
    content = f.read()

# Replace the empty space with the verified table rows
new_content = content.replace('', table_data)

with open('/data/data/com.termux/files/home/humbu_community_nexus/index.html', 'w') as f:
    f.write(new_content)

print("✅ Fleet Data Injected into Dashboard")
