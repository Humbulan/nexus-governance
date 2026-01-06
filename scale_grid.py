#! /usr/bin/env python3
import json
import os

grid_path = os.path.expanduser('~/humbu_community_nexus/gauteng_grid.json')
nodes = {f"NODE_{i}": {"status": "READY", "capacity": "SURGE"} for i in range(1, 21)}

with open(grid_path, 'w') as f:
    json.dump(nodes, f, indent=4)
print("✅ Gauteng Power Grid: 20/20 Nodes Provisioned")
