import subprocess

def check_firewall():
    result = subprocess.run(['sudo', 'ufw', 'status'], capture_output=True, text=True)
    if 'inactive' in result.stdout:
        print("Firewall is inactive!")
    else:
        print("Firewall is active.")

def check_antivirus():
    result = subprocess.run(['systemctl', 'status', 'clamav-daemon'], capture_output=True, text=True)
    if 'active (running)' in result.stdout:
        print("Antivirus is running.")
    else:
        print("Antivirus is not running!")

check_firewall()
check_antivirus()
