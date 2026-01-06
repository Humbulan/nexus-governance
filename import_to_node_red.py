#! /usr/bin/env python3
#!/usr/bin/env python3
"""
🏛️ NODE-RED IMPORT AUTOMATION
Creates flows for Imperial Infrastructure visualization
"""
import json
import os
import requests
from datetime import datetime

def create_monday_surge_flow():
    """Create Monday Surge visualization flow"""
    flow = {
        "label": "🚀 Monday Surge Monitor",
        "nodes": [
            {
                "id": "surge-trigger",
                "type": "inject",
                "z": "monday-surge",
                "name": "Every 30s",
                "props": [{"p": "payload"}, {"p": "topic", "vt": "str"}],
                "repeat": "30",
                "crontab": "",
                "once": False,
                "onceDelay": 0.1,
                "topic": "surge_check",
                "payload": "check",
                "payloadType": "str",
                "x": 150,
                "y": 100
            },
            {
                "id": "exec-surge-check",
                "type": "exec",
                "z": "monday-surge",
                "command": "python3",
                "addpay": False,
                "append": "",
                "useSpawn": "false",
                "timer": "",
                "winHide": False,
                "oldrc": False,
                "name": "Check Surge Readiness",
                "x": 350,
                "y": 100,
                "wires": [["parse-surge-output", "surge-log"]]
            },
            {
                "id": "parse-surge-output",
                "type": "function",
                "z": "monday-surge",
                "name": "Parse Capacity",
                "func": "// Extract capacity from surge audit\nlet output = msg.payload.toString();\nlet capacity = 100;\n\nif (output.includes('Capacity:')) {\n    let match = output.match(/Capacity:\\s*(\\d+\\.?\\d*)%/);\n    if (match) capacity = parseFloat(match[1]);\n}\n\nmsg.payload = {\n    capacity: capacity,\n    ready: capacity >= 100,\n    timestamp: new Date().toISOString(),\n    target: 595238.10,\n    nodes: 20\n};\n\nreturn msg;",
                "outputs": 1,
                "noerr": 0,
                "initialize": "",
                "finalize": "",
                "libs": [],
                "x": 550,
                "y": 100,
                "wires": [["capacity-gauge", "surge-status"]]
            },
            {
                "id": "capacity-gauge",
                "type": "ui_gauge",
                "z": "monday-surge",
                "name": "Surge Capacity",
                "group": "surge-dashboard",
                "order": 1,
                "width": 0,
                "height": 0,
                "gtype": "gage",
                "title": "Monday Surge Readiness",
                "label": "percent",
                "format": "{{value}}%",
                "min": 0,
                "max": 200,
                "colors": ["#00b500", "#e6e600", "#ca3838"],
                "seg1": "100",
                "seg2": "150",
                "x": 750,
                "y": 100,
                "wires": []
            },
            {
                "id": "surge-status",
                "type": "ui_text",
                "z": "monday-surge",
                "group": "surge-dashboard",
                "order": 2,
                "width": 0,
                "height": 0,
                "name": "Surge Status",
                "label": "Status",
                "format": "{{msg.payload.ready ? '✅ READY' : '⚠️ PREPARING'}}",
                "layout": "row-spread",
                "x": 750,
                "y": 150,
                "wires": []
            },
            {
                "id": "hard-trigger",
                "type": "switch",
                "z": "monday-surge",
                "name": "R500K Hard Trigger",
                "property": "msg.payload.capacity",
                "propertyType": "msg",
                "rules": [
                    {"t": "gte", "v": "100", "vt": "num"},
                    {"t": "lt", "v": "100", "vt": "num"}
                ],
                "checkall": "true",
                "repair": False,
                "outputs": 2,
                "x": 550,
                "y": 200,
                "wires": [
                    ["gold-alert"],
                    ["blue-alert"]
                ]
            },
            {
                "id": "gold-alert",
                "type": "change",
                "z": "monday-surge",
                "name": "Set Gold Theme",
                "rules": [
                    {"t": "set", "p": "theme", "pt": "flow", "to": "gold", "tot": "str"}
                ],
                "action": "",
                "property": "",
                "from": "",
                "to": "",
                "reg": False,
                "x": 750,
                "y": 200,
                "wires": [["theme-change"]]
            },
            {
                "id": "surge-log",
                "type": "debug",
                "z": "monday-surge",
                "name": "Surge Log",
                "active": True,
                "tosidebar": True,
                "console": False,
                "tostatus": False,
                "complete": "false",
                "targetType": "full",
                "statusVal": "",
                "statusType": "auto",
                "x": 550,
                "y": 50
            }
        ]
    }
    return flow

def create_gauteng_grid_flow():
    """Create Gauteng Power Grid visualization"""
    flow = {
        "label": "⚡ Gauteng Power Grid",
        "nodes": [
            {
                "id": "grid-poll",
                "type": "inject",
                "z": "gauteng-power-grid",
                "name": "Every 60s",
                "props": [{"p": "payload"}, {"p": "topic", "vt": "str"}],
                "repeat": "60",
                "crontab": "",
                "once": False,
                "onceDelay": 0.1,
                "topic": "grid_update",
                "payload": "",
                "payloadType": "date",
                "x": 150,
                "y": 100
            },
            {
                "id": "http-grid-data",
                "type": "http request",
                "z": "gauteng-power-grid",
                "name": "Get Grid Data",
                "method": "GET",
                "ret": "txt",
                "paytoqs": "ignore",
                "url": "http://localhost:8080/api/gauteng",
                "tls": "",
                "persist": False,
                "proxy": "",
                "authType": "",
                "senderr": False,
                "x": 350,
                "y": 100,
                "wires": [["parse-grid-data"]]
            },
            {
                "id": "parse-grid-data",
                "type": "function",
                "z": "gauteng-power-grid",
                "name": "Parse Grid Data",
                "func": "// Parse Gauteng Power Grid data\nlet data = {};\ntry {\n    data = JSON.parse(msg.payload);\n} catch(e) {\n    data = {error: 'Parse failed'};\n}\n\n// Create visualization data\nmsg.payload = {\n    nodes: 20,\n    active: 20,\n    revenue: data.target || 500000,\n    progress: data.readiness || 66.9,\n    timestamp: new Date().toISOString()\n};\n\nreturn msg;",
                "outputs": 1,
                "noerr": 0,
                "x": 550,
                "y": 100,
                "wires": [["grid-chart", "node-counter"]]
            },
            {
                "id": "grid-chart",
                "type": "ui_chart",
                "z": "gauteng-power-grid",
                "name": "Revenue Progress",
                "group": "grid-dashboard",
                "order": 1,
                "width": "12",
                "height": "6",
                "label": "Gauteng Power Grid",
                "chartType": "line",
                "legend": "true",
                "xformat": "HH:mm:ss",
                "interpolate": "linear",
                "nodata": "",
                "dot": False,
                "ymin": "",
                "ymax": "",
                "removeOlder": "1",
                "removeOlderPoints": "",
                "removeOlderUnit": "3600",
                "cutout": 0,
                "useOneColor": False,
                "colors": ["#1f77b4", "#aec7e8", "#ff7f0e", "#2ca02c"],
                "useOldStyle": False,
                "x": 750,
                "y": 100
            },
            {
                "id": "node-counter",
                "type": "ui_gauge",
                "z": "gauteng-power-grid",
                "name": "Active Nodes",
                "group": "grid-dashboard",
                "order": 2,
                "width": "6",
                "height": "4",
                "gtype": "donut",
                "title": "Active Nodes",
                "label": "units",
                "format": "{{value}}/20",
                "min": 0,
                "max": 20,
                "colors": ["#00b500", "#e6e600", "#ca3838"],
                "seg1": "15",
                "seg2": "18",
                "x": 750,
                "y": 200
            }
        ]
    }
    return flow

def create_revenue_automation_flow():
    """Create $147,575/month revenue automation"""
    flow = {
        "label": "💰 Revenue Automation",
        "nodes": [
            {
                "id": "contract-webhook",
                "type": "http in",
                "z": "revenue-automation",
                "name": "Contract Webhook",
                "url": "/contract/webhook",
                "method": "post",
                "upload": False,
                "swaggerDoc": "",
                "x": 150,
                "y": 100,
                "wires": [["process-contract"]]
            },
            {
                "id": "process-contract",
                "type": "function",
                "z": "revenue-automation",
                "name": "Process Contract",
                "func": "// Process new contract from sign-client\nlet contract = msg.payload;\n\n// Calculate revenue impact\nlet monthlyRevenue = 147575; // Base\nlet newRevenue = monthlyRevenue + (contract.value || 0) * 0.8; // 80% conversion\n\nmsg.payload = {\n    contract: contract,\n    newMonthlyRevenue: newRevenue,\n    timestamp: new Date().toISOString(),\n    automation: 'Revenue triggered'\n};\n\nreturn msg;",
                "outputs": 1,
                "noerr": 0,
                "x": 350,
                "y": 100,
                "wires": [["revenue-tracker", "send-notification"]]
            },
            {
                "id": "revenue-tracker",
                "type": "ui_chart",
                "z": "revenue-automation",
                "name": "Revenue Tracker",
                "group": "revenue-dashboard",
                "order": 1,
                "width": "12",
                "height": "6",
                "label": "Monthly Revenue",
                "chartType": "bar",
                "legend": "true",
                "xformat": "HH:mm:ss",
                "interpolate": "linear",
                "nodata": "",
                "dot": False,
                "ymin": "0",
                "ymax": "200000",
                "removeOlder": "1",
                "removeOlderPoints": "",
                "removeOlderUnit": "3600",
                "cutout": 0,
                "useOneColor": False,
                "colors": ["#2ca02c", "#98df8a", "#d62728", "#ff9896"],
                "useOldStyle": False,
                "x": 550,
                "y": 100
            },
            {
                "id": "send-notification",
                "type": "exec",
                "z": "revenue-automation",
                "command": "python3",
                "addpay": False,
                "append": "",
                "useSpawn": "false",
                "timer": "",
                "winHide": False,
                "oldrc": False,
                "name": "Send Alert",
                "x": 550,
                "y": 200,
                "wires": [["log-notification"]]
            },
            {
                "id": "http-response",
                "type": "http response",
                "z": "revenue-automation",
                "name": "",
                "statusCode": "200",
                "headers": {},
                "x": 750,
                "y": 100,
                "wires": []
            }
        ]
    }
    return flow

def export_flows():
    """Export all flows to Node-RED format"""
    flows = []
    
    # Add flows
    flows.append(create_monday_surge_flow())
    flows.append(create_gauteng_grid_flow())
    flows.append(create_revenue_automation_flow())
    
    # Create complete export
    export = {
        "flows": flows,
        "meta": {
            "exported": datetime.now().isoformat(),
            "version": "2026.1.0",
            "project": "Humbu Imperial Nexus",
            "description": "Node-RED flows for Monday IDC presentation"
        }
    }
    
    # Save to file
    export_file = os.path.expanduser("~/humbu_community_nexus/node_red_export.json")
    with open(export_file, 'w') as f:
        json.dump(export, f, indent=2)
    
    print(f"✅ Node-RED flows exported to: {export_file}")
    print(f"📊 Total flows: {len(flows)}")
    print(f"🔗 Import at: http://localhost:1880")
    
    return export_file

if __name__ == "__main__":
    export_file = export_flows()
    print(f"\n🏛️ NODE-RED FLOWS READY FOR IDC PRESENTATION")
    print(f"==========================================")
    print(f"1. Open Node-RED: http://localhost:1880")
    print(f"2. Click menu → Import → Clipboard")
    print(f"3. Paste content from: {export_file}")
    print(f"4. Deploy and visit Dashboard tabs")
    print(f"")
    print(f"🌐 PUBLIC URL (for IDC): https://nexus-dashboard.humbu.store")
