#Arduino Uno Q

import socket
import subprocess
from datetime import datetime
import platform
import hashlib
from pathlib import Path

def get_hostname():
    return socket.gethostname()
def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except socket.error:
        return "Unknown"

def run_cmd(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL)
    except Exception:
        return "Unavailable"

def check_internet_connection():
    result = subprocess.run(
   ["ping", "-c", "1", "8.8.8.8"],
         stdout=subprocess.DEVNULL,
         stderr=subprocess.DEVNULL
    )
    return result.returncode == 0
def log_status():
    hostname = get_hostname()
    online = check_internet_connection()
    timestamp = datetime.now()

    with open("status.log", "a") as file:
        file.write(f"{timestamp}\t{hostname}\t{online}\n")

    print("Status saved correctly.")

def show_status():
    print("\n=== UNO Q STATUS ===")
    print("Hostname:", get_hostname())
    print("OS:", platform.system(), platform.release())
    print("Version:", platform.version())
    print("Internet online:", check_internet_connection())

def mac_address_scan():
    print("\n=== MAC ADDRESS/ARP SCAN ===")
    print(run_cmd("arp -a"))

def incident_snapshot():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"incident_snapshot_{timestamp}.txt"

    report = []
    report.append("=== UNO Q SENTINEL INCIDENT SNAPSHOT ===")
    report.append(f"Timestamp: {datetime.now()}")
    report.append(f"Hostname: {get_hostname()}")
    report.append(f"OS: {platform.system()} {platform.release()}")
    report.append(f"Version: {platform.version()}")
    report.append(f"IP: {get_ip()}")
    report.append("\n=== ARP TABLE ===")
    report.append(run_cmd("arp -a"))
    report.append("\n=== USERS ===")
    report.append("\n=== PROCESSES ===")
    report.append(run_cmd("who"))
    report.append("\n=== PROCESSES ===")
    report.append(run_cmd("ps aux | head -30"))
    report.append("\n=== NETWORK CONNECTIONS ===")
    report.append(run_cmd("ss -tunap 2>/dev/null || netstat -an"))

    Path(filename).write_text("\n".join(report))
    print(f"Snapshot saved correctly. {filename}")

def hash_file():
    path = input("File path to the hash: ").strip()
    p = Path(path)

    if not p.is_file():
        print("File does not exist")
        return

    h = hashlib.sha256()

    with open(p, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            h.update(chunk)
    print("SHA256:", h.hexdigest())

def main():
    while True:
        print()
        print("=== UNO Q SENTINEL CYBERDECK ===")
        print("1- Show hostname")
        print("2- Show IP")
        print("3- Check Internet Connection")
        print("4- Show status")
        print("5- Save status log")
        print("6- MAC ADDRESS/ARP SCAN")
        print("7- Incident Snapshot")
        print("8- Hash Summary")
        print("9- Exit")

        choice = input("> ")
        if choice == "1":
            print(get_hostname())
        elif choice == "2":
            print(get_ip())
        elif choice == "3":
            print("Internet online", check_internet_connection())
        elif choice == "4":
            show_status()
        elif choice == "5":
            log_status()
        elif choice == "6":
            mac_address_scan()
        elif choice == "7":
            incident_snapshot()
        elif choice == "8":
            hash_file()
        elif choice == "9":
            print("Exit")
            break
        else:
            print("Invalid choice")
main()










