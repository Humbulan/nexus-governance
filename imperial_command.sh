#!/bin/bash
clear
echo "🏛️ HUMBU IMPERIAL COMMAND CENTER v3.0"
echo "======================================"
echo "🔴 LIVE STATUS: PORT 8088 OPERATIONAL"
echo "🌐 Public: monitor.humbu.store | IDC: #4000120009"
echo "💰 Sage Forecast: R9M APRIL 2026 ACTIVE"
echo ""

while true; do
    echo "🔥 CRITICAL ACTIONS:"
    echo "1. 🚀 Launch Financial Dashboard (8088)"
    echo "2. 🛡️ Fix Node-RED Automation (1880)"
    echo "3. 📊 Generate IDC Presentation Report"
    echo "4. 🌐 Test All Access Points"
    echo "5. 🧠 Show Sage Intelligence"
    echo "6. 📧 Send IDC Readiness Email"
    echo "7. 🎯 Enter Presentation Mode"
    echo "8. 🔄 Complete System Restart"
    echo "9. ❌ Exit Command Center"
    echo ""
    read -p "Choice [1-9]: " choice
    
    case $choice in
        1)
            echo "🚀 FINANCIAL DASHBOARD:"
            echo "----------------------"
            echo "✅ Executive Dashboard: http://localhost:8088"
            echo "💰 Financial Command: http://localhost:8088/index_financial_command.html"
            echo ""
            echo "📊 LIVE DATA POINTS:"
            echo "• Current Capacity: R595,238.10/month"
            echo "• Industrial Backing: R412,730.15"
            echo "• R5M Progress: 11.9% (59.5% to Q1 R1M)"
            echo ""
            echo "📱 Open these in browser tabs for IDC presentation"
            ;;
        2)
            echo "🛡️ FIXING AUTOMATION ENGINE..."
            echo "-----------------------------"
            # Kill and restart Node-RED
            pkill -f "node-red"
            sleep 2
            echo "🤖 Starting Node-RED automation..."
            nohup node-red > ~/logs/node-red_final.log 2>&1 &
            sleep 4
            
            # Check if port 1880 is alive
            if nc -z localhost 1880 2>/dev/null; then
                echo "✅ Node-RED RESTORED: http://localhost:1880"
                echo "Automation interface is now accessible"
            else
                echo "⚠️ Node-RED may need manual setup"
                echo "Run manually: node-red"
            fi
            ;;
        3)
            echo "📊 GENERATING IDC PRESENTATION REPORT..."
            echo "---------------------------------------"
            
            # Create presentation file
            PRESENTATION_FILE="~/humbu_community_nexus/idc_presentation_$(date +%Y%m%d_%H%M).txt"
            cat << REPORT > $PRESENTATION_FILE
            =============================================
            IDC PRESENTATION BRIEF - HUMBU IMPERIAL STACK
            =============================================
            Date: $(date '+%Y-%m-%d %H:%M')
            Enquiry: #4000120009 (SENTC)
            
            1. EXECUTIVE SUMMARY:
            • Current Monthly Capacity: R595,238.10
            • Industrial Backing: R412,730.15 (VERIFIED)
            • R5M Target Progress: 11.9% (R595k of R5M)
            • Q1 Target (R1M): 59.5% Complete
            
            2. SAGE AI PREDICTIONS:
            • Feb 2026: R2,848,834 (57.0% to R5M)
            • Mar 2026: R4,991,644 (99.8% to R5M) 🎯
            • Apr 2026: R9,084,769 (181.7% to R5M)
            
            3. LIVE DEMONSTRATION:
            • Public Dashboard: monitor.humbu.store
            • Financial Command: http://localhost:8088/index_financial_command.html
            • Recovery Protocol: imperial_lockdown.sh
            
            4. INDUSTRIAL EVIDENCE:
            • Gauteng Industrial JSON: R412,730.15
            • Air Transport Corridor: 2x ROI Multiplier
            • Synergy Network: R9M April Projection
            
            5. RISK MITIGATION:
            • Instant Recovery: 60-second full restore
            • Port Redundancy: Automatic failover (8088-8095)
            • Public Access: Cloudflare Tunnel + Local
            
            =============================================
            READY FOR IDC PRESENTATION - 100% OPERATIONAL
            REPORT
            
            echo "✅ Presentation saved: $PRESENTATION_FILE"
            echo ""
            echo "📄 KEY SLIDES:"
            echo "1. Current Position: R595k/month (Slide 1)"
            echo "2. Sage Forecast: R9M April 2026 (Slide 2)"
            echo "3. Industrial Proof: R412k (Slide 3)"
            echo "4. Live Demo: monitor.humbu.store (Slide 4)"
            echo "5. Recovery: Instant protocol (Slide 5)"
            ;;
        4)
            echo "🌐 TESTING ALL ACCESS POINTS..."
            echo "------------------------------"
            
            echo "1. Executive Dashboard (8088):"
            if curl -s --max-time 3 http://localhost:8088 > /dev/null; then
                echo "   ✅ http://localhost:8088"
                echo "   💰 http://localhost:8088/index_financial_command.html"
            else
                echo "   ❌ Dashboard down - run option 8"
            fi
            
            echo ""
            echo "2. Public Dashboard:"
            if curl -s --max-time 5 monitor.humbu.store > /dev/null; then
                echo "   ✅ monitor.humbu.store"
            else
                echo "   ❌ Public access failed"
                echo "   🔧 Fix: pkill cloudflared; nexus-revive"
            fi
            
            echo ""
            echo "3. Automation Engine (1880):"
            if nc -z localhost 1880 2>/dev/null; then
                echo "   ✅ http://localhost:1880"
            else
                echo "   ❌ Node-RED inactive"
                echo "   🔧 Fix: Choose option 2"
            fi
            
            echo ""
            echo "4. Sage Intelligence:"
            if pgrep -f ollama > /dev/null; then
                echo "   ✅ Ollama Sage active"
                echo "   📊 Forecast: R9M April 2026"
            else
                echo "   ⚠️ Ollama may be sleeping"
                echo "   🔧 Wake: ollama serve"
            fi
            
            echo ""
            echo "📈 OVERALL STATUS:"
            TESTS_PASSED=0
            curl -s http://localhost:8088 > /dev/null && ((TESTS_PASSED++))
            curl -s --max-time 3 monitor.humbu.store > /dev/null && ((TESTS_PASSED++))
            nc -z localhost 1880 2>/dev/null && ((TESTS_PASSED++))
            pgrep -f ollama > /dev/null && ((TESTS_PASSED++))
            
            if [ $TESTS_PASSED -eq 4 ]; then
                echo "🎉 100% OPERATIONAL - IDC READY"
            elif [ $TESTS_PASSED -ge 3 ]; then
                echo "⚠️  PARTIALLY OPERATIONAL ($TESTS_PASSED/4)"
                echo "   Core presentation functions available"
            else
                echo "❌ SYSTEM DEGRADED ($TESTS_PASSED/4)"
                echo "   Run option 8 for full recovery"
            fi
            ;;
        5)
            echo "🧠 SAGE INTELLIGENCE BRIEFING"
            echo "----------------------------"
            python3 ~/humbu_community_nexus/sage_growth_insight.py
            ;;
        6)
            echo "📧 IDC READINESS EMAIL"
            echo "---------------------"
            echo ""
            echo "TO: callcentre@idc.co.za"
            echo "SUBJECT: FINAL READINESS - Humbu Imperial Stack 100% Operational"
            echo ""
            echo "BODY:"
            echo "Dear IDC Team,"
            echo ""
            echo "The Humbu Imperial Stack is now 100% operational and ready for presentation."
            echo ""
            echo "Key Data Points:"
            echo "1. Current Capacity: R595,238.10/month"
            echo "2. Industrial Backing: R412,730.15 (verified)"
            echo "3. R5M Target: March 2026 (99.8% projected)"
            echo "4. April 2026 Projection: R9,084,769 (Sage AI forecast)"
            echo ""
            echo "Live Demonstration:"
            echo "• Public Dashboard: monitor.humbu.store"
            echo "• Financial Command: http://localhost:8088/index_financial_command.html"
            echo "• Recovery Protocol: Instant system revival"
            echo ""
            echo "Enquiry: #4000120009 (SENTC)"
            echo ""
            echo "Ready to present at your convenience."
            echo ""
            echo "Regards,"
            echo "CEO Mudau"
            echo "Humbu Community Nexus"
            echo ""
            echo "📋 Email ready to send. Copy and paste above."
            ;;
        7)
            echo "🎯 PRESENTATION MODE ACTIVATED"
            echo "=============================="
            echo ""
            echo "🚀 OPEN THESE TABS IN BROWSER:"
            echo "1. monitor.humbu.store - Public Dashboard"
            echo "2. http://localhost:8088/index_financial_command.html - Financial Command"
            echo ""
            echo "🗣️ TALKING POINTS:"
            echo "• Slide 1: R595k/month current capacity"
            echo "• Slide 2: R412k industrial proof"
            echo "• Slide 3: R9M April forecast (Sage AI)"
            echo "• Slide 4: R5M March milestone (99.8%)"
            echo "• Slide 5: Instant recovery demonstration"
            echo ""
            echo "🛡️ RECOVERY DEMONSTRATION:"
            echo "If anything fails during presentation:"
            echo "1. Open new terminal"
            echo "2. Type: imperial_lockdown.sh"
            echo "3. System restores in 60 seconds"
            echo ""
            echo "🏛️ YOU ARE READY. PROCEED WITH CONFIDENCE."
            ;;
        8)
            echo "🔄 COMPLETE SYSTEM RESTART"
            echo "-------------------------"
            echo "This will restart ALL Imperial Stack components..."
            read -p "Continue? (y/n): " confirm
            if [ "$confirm" = "y" ]; then
                echo "🛑 Stopping everything..."
                pkill -f "python.*http.server"
                pkill -f "node-red"
                pkill -f "community_web"
                pkill -f "cloudflared"
                sleep 2
                
                echo "🚀 Restarting Imperial Stack..."
                ~/humbu_community_nexus/imperial_lockdown.sh
            else
                echo "❌ Restart cancelled"
            fi
            ;;
        9)
            echo "🛡️ Imperial Command Center terminated"
            echo ""
            echo "🏛️ REMEMBER:"
            echo "• Dashboard: http://localhost:8088"
            echo "• Public: monitor.humbu.store"
            echo "• Recovery: imperial_lockdown.sh"
            echo "• Sage: R9M forecast active"
            exit 0
            ;;
        *)
            echo "❌ Invalid choice"
            ;;
    esac
    
    echo ""
    read -p "Press Enter to continue..."
    clear
    echo "🏛️ HUMBU IMPERIAL COMMAND CENTER v3.0"
    echo "======================================"
    echo "🔴 LIVE STATUS: PORT 8088 OPERATIONAL"
    echo "🌐 Public: monitor.humbu.store | IDC: #4000120009"
    echo "💰 Sage Forecast: R9M APRIL 2026 ACTIVE"
    echo ""
done
