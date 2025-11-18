#!/usr/bin/env python3
import os
import time
import random
import sys
from datetime import datetime

def clear_screen():
    os.system('clear')

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def banner():
    # CRYPTICX Banner
    crypticx_banner = r"""
     ██████ ██████  ██    ██ ██████  ████████ ██  ██████ ██   ██ 
    ██      ██   ██  ██  ██  ██   ██    ██    ██ ██      ██  ██  
    ██      ██████    ████   ██████     ██    ██ ██      █████   
    ██      ██   ██    ██    ██         ██    ██ ██      ██  ██  
     ██████ ██   ██    ██    ██         ██    ██  ██████ ██   ██ 
    """
    
    # Haq Cyber Squad Banner
    haq_banner = r"""
    ░█░█░█▀█░▄▀▄░░░█▀▀░█░█░█▀▄░█▀▀░█▀▄░░░█▀▀░▄▀▄░█░█░█▀█░█▀▄
    ░█▀█░█▀█░█\█░░░█░░░░█░░█▀▄░█▀▀░█▀▄░░░▀▀█░█\█░█░█░█▀█░█░█
    ░▀░▀░▀░▀░░▀\░░░▀▀▀░░▀░░▀▀░░▀▀▀░▀░▀░░░▀▀▀░░▀\░▀▀▀░▀░▀░▀▀░                                                                                                            
    """
    
    clear_screen()
    
    # CRYPTICX Display
    print(color_text("═" * 60, '1;36'))
    for line in crypticx_banner.split('\n'):
        print(color_text(line, '1;35'))
    
    # Haq Cyber Squad Display
    for line in haq_banner.split('\n'):
        print(color_text(line, '1;36'))
    
    print(color_text("═" * 60, '1;36'))

def cyber_scan():
    scans = [
        "🛡️  HAQ CYBER SECURITY SCAN INITIATED",
        "🔍 Analyzing system vulnerabilities...",
        "📡 Monitoring network interfaces...",
        "🔒 Checking encryption protocols...",
        "💾 Verifying memory integrity...",
        "🌐 Testing connection security...",
        "⚡ Optimizing cyber defenses...",
        "🔄 Finalizing security audit..."
    ]
    
    for scan in scans:
        print(color_text("⟳ ", '1;34') + color_text(scan, '1;33'))
        time.sleep(0.6)

def progress_bar():
    stages = [
        ("INITIALIZING", 20),
        ("SCANNING", 40),
        ("ANALYZING", 60),
        ("SECURING", 80),
        ("COMPLETED", 100)
    ]
    
    print("\n" + color_text("🚀 CYBER BOOT SEQUENCE:", '1;32'))
    
    for stage_name, progress in stages:
        bars = "▰" * (progress // 4) + "▱" * (25 - (progress // 4))
        sys.stdout.write(f"\r[{bars}] {progress}% - {stage_name} ")
        sys.stdout.flush()
        time.sleep(0.5)
    
    print()

def display_info():
    print("\n" + color_text("🏴 HAQ CYBER SQUAD - CRYPTICX", '1;33'))
    print(color_text("═" * 45, '1;36'))
    
    info = {
        "👤 Operator": os.getenv('USER', 'CRYPTICX'),
        "📟 Terminal": "iSH Shell",
        "🐧 Platform": "Alpine Linux",
        "🔐 Security": "LEVEL 4",
        "🎯 Mission": "Cyber Defense",
        "🕐 Time": datetime.now().strftime("%H:%M:%S")
    }
    
    for key, value in info.items():
        print(color_text(f"{key}: ", '1;32') + color_text(f"{value}", '1;37'))
        time.sleep(0.2)

def main():
    try:
        # Show banner
        banner()
        time.sleep(1)
        
        # Cyber scan
        cyber_scan()
        time.sleep(1)
        
        # Progress bar
        progress_bar()
        time.sleep(1)
        
        # Display info
        display_info()
        time.sleep(2)
        
        print(color_text("\n🎯 SYSTEM READY FOR CYBER OPERATIONS", '1;32'))
        print(color_text("💻 Type 'help' for available commands\n", '1;36'))
        
    except KeyboardInterrupt:
        print(color_text("\n\n⏹️  Operation cancelled", '1;31'))
    except Exception as e:
        print(color_text(f"\n\n❌ Error: {e}", '1;31'))

if __name__ == "__main__":
    main()
