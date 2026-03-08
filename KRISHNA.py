import psutil
import os
import socket
import time
from colorama import Fore, Style, init

# Colors initialize
init(autoreset=True)

# --- Configuration ---
LOG_FILE = "KRISHNA_Report.txt"
WHITELIST = ['KRISHNA.py', 'KRISHNA_Report.txt', 'Run_KRISHNA.bat']
CRITICAL_KEYS = ['eval(', 'exec(', 'socket.connect', 'os.system', 'subprocess']
# In folders ko skip karenge taaki VS Code aur System logs interference na karein
IGNORE_DIRS = ['Diagnostics', 'vscode-stable-user-x64', 'Microsoft', 'Windows', 'Temp\\_MEI']

def get_admin():
    import ctypes
    try: return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except: return False

def progress_bar(text):
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}[*] {text}")
    print(f"{Fore.WHITE}    Status: [", end="", flush=True)
    for _ in range(25):
        time.sleep(0.005)
        print(f"{Fore.CYAN}█", end="", flush=True)
    print(f"{Fore.WHITE}] 100%\n")

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    divine_art = f"""
{Fore.GREEN}           .---.
{Fore.GREEN}          /     \\      {Fore.CYAN}  ____
{Fore.GREEN}          \\      /    {Fore.CYAN}  (_    _)
{Fore.GREEN}           |    |    {Fore.CYAN}    /  /
{Fore.GREEN}           |    |   {Fore.CYAN}    /  /
{Fore.GREEN}           |    |  {Fore.CYAN}    /  /     {Fore.YELLOW}  __________________________________________
{Fore.GREEN}           |    | {Fore.CYAN}    /  /      {Fore.YELLOW} (__________________________________________)
{Fore.GREEN}           |____|{Fore.CYAN}____/  /       {Fore.YELLOW}  |  |  |  |  |  |  |  |  |  |  |  |  |  |
{Fore.GREEN}           (____){Fore.CYAN}______/        {Fore.YELLOW}  '--'--'--'--'--'--'--'--'--'--'--'--'--'--'
    """
    print(divine_art)
    print(f"{Fore.CYAN}{Style.BRIGHT}═{'═'*55}═")
    print(f"{Fore.WHITE}{Style.BRIGHT}      🔱 PROJECT: KRISHNA (Forensics v4.1) 🔱")
    print(f"{Fore.CYAN}{Style.BRIGHT}═{'═'*55}═")
    print(f"{Fore.GREEN}      [ Intelligence: ACTIVE ] [ Dev: @thesudosiuu ]")
    print(f"{Fore.CYAN}{Style.BRIGHT}═{'═'*55}═")

def scan_file_turbo(file_path):
    found = False
    try:
        with open(file_path, 'r', errors='ignore') as f:
            for i, line in enumerate(f):
                if i > 1000: break # Turbo Speed filter
                for key in CRITICAL_KEYS:
                    if key in line:
                        found = True
                        print(f"{Fore.RED}[!] CRITICAL THREAT: Found '{key}'")
                        print(f"{Fore.YELLOW}    Line {i+1}: {Fore.WHITE}{line.strip()[:60]}...")
                        print(f"{Fore.CYAN}    Path: {file_path}\n")
                if 'base64' in line and any(k in line for k in ['eval', 'exec', 'decode']):
                    found = True
                    print(f"{Fore.LIGHTRED_EX}[!] SUSPICIOUS: Encoded Payload (Base64)")
                    print(f"{Fore.CYAN}    Path: {file_path}\n")
        return found
    except: return False

def trace_origin():
    progress_bar("PHASE 1: Forensic Malware Inspection")
    threat_count, file_count = 0, 0
    user_name = os.getlogin()
    target_paths = [
        f'C:\\Users\\{user_name}\\Desktop',
        f'C:\\Users\\{user_name}\\Downloads',
        f'C:\\Users\\{user_name}\\AppData\\Local\\Temp'
    ]

    for path in target_paths:
        if not os.path.exists(path): continue
        for root, dirs, files in os.walk(path):
            if any(ignored in root for ignored in IGNORE_DIRS): continue
            for file in files:
                if file in WHITELIST or 'Setup Log' in file: continue
                # Sirf potential scripts ko scan karega fast scanning ke liye
                if file.endswith(('.py', '.bat', '.ps1', '.js', '.vbs', '.exe')):
                    file_count += 1
                    if scan_file_turbo(os.path.join(root, file)):
                        threat_count += 1
    
    print(f"{Fore.WHITE}--- PHASE 1 SUMMARY ---")
    print(f"{Fore.GREEN}[+] Files Analyzed: {file_count}")
    if threat_count == 0:
        print(f"{Fore.CYAN}[✓] Status: No Malware Found in Files.")
    else:
        print(f"{Fore.RED}[!] Status: {threat_count} Threats detected in local files.")
    return threat_count

def check_network():
    progress_bar("PHASE 2: Network Intelligence Analysis")
    unknown_conns = 0
    # Expand list: added 4., 57., and other MS/CDN ranges
    trusted = ['142.', '172.', '49.', '54.', '34.', '13.', '20.', '40.', '52.', '104.', '23.', '135.', '185.', '4.', '57.']

    try:
        for conn in psutil.net_connections(kind='inet'):
            if conn.status == 'ESTABLISHED' and conn.raddr:
                ip = conn.raddr[0] if isinstance(conn.raddr, tuple) else conn.raddr.ip
                if ip.startswith(('127.', '192.168.', '10.', '172.16.')) or ip == '::1': continue
                
                is_trusted = any(ip.startswith(p) for p in trusted)
                if not is_trusted:
                    print(f"{Fore.RED}[!] UNKNOWN CONNECTION: {ip}")
                    unknown_conns += 1
        
        if unknown_conns == 0:
            print(f"{Fore.GREEN}[✓] Status: All network traffic appears verified.")
    except: pass
    return unknown_conns

def divine_message(total_threats):
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}--- Divine Message ---")
    if total_threats > 0:
        # Threat Message
        print(f"{Fore.RED}\"Paritranaya sadhunam vinashaya cha dushkritam\"")
        print(f"{Fore.CYAN}English: \"To protect the righteous and to destroy the wicked.\"")
        print(f"{Fore.RED}\n[ ALERT ] System integrity compromised. Purge required.")
    else:
        # Clean Message
        print(f"{Fore.GREEN}\"Sarve bhavantu sukhinah, sarve santu niramayah\"")
        print(f"{Fore.CYAN}English: \"May all be happy, may all be free from illness/evil.\"")
        print(f"{Fore.GREEN}\n[ SECURE ] Your digital sanctuary is safe.")
    print(f"{Fore.CYAN}{Style.BRIGHT}═{'═'*55}═")

if __name__ == "__main__":
    banner()
    if get_admin():
        f1_threats = trace_origin()
        f2_threats = check_network()
        divine_message(f1_threats + f2_threats)
    else:
        print(f"{Fore.RED}[X] CRITICAL ERROR: PLEASE RUN AS ADMINISTRATOR.")