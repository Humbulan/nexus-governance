#!/bin/bash
while true; do
    # Rotate vehicle statuses
    cd ~/humbu_community_nexus
    python3 -c "
import json, random, time
with open('fleet_data.json', 'r') as f:
    data = json.load(f)

# Update timestamp
current_time = time.strftime('%H:%M:%S')
data['last_update'] = time.strftime('%Y-%m-%dT%H:%M:%S.000Z')
data['metrics']['last_system_update'] = current_time

# Randomly update some vehicles
statuses = ['In Transit', 'Loading', 'Unloading', 'Returning', 'Route Optimizing']
for vehicle in data['fleet']:
    if random.random() < 0.2:  # 20% chance to change status
        vehicle['status'] = random.choice(statuses)
        vehicle['last_update'] = current_time
        vehicle['temp'] = f'{random.randint(20, 49)/10:.1f}°C'

with open('fleet_data.json', 'w') as f:
    json.dump(data, f, indent=2)
print(f'🔄 Fleet data updated at {current_time}')
"
    sleep 30
done
