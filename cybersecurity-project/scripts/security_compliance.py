import subprocess
import os

def check_firewall_status():
    try:
        result = subprocess.run(["ufw", "status"], capture_output=True, text=True)
        if "Status: active" in result.stdout:
            return "✅ UFW Firewall is active."
        else:
            return "❌ UFW Firewall is NOT active."
    except FileNotFoundError:
        return "⚠️ UFW not installed."

def check_ssh_root_login():
    try:
        with open("/etc/ssh/sshd_config", 'r') as f:
            content = f.read()
            if "PermitRootLogin no" in content:
                return "✅ Root login over SSH is disabled."
            else:
                return "❌ Root login over SSH is ENABLED."
    except FileNotFoundError:
        return "⚠️ SSH configuration file not found."

def save_compliance_report(results, output_file):
    with open(output_file, 'a') as f:
        f.write("\n\n--- Security Compliance Check ---\n")
        for item in results:
            f.write(f"{item}\n")

def main():
    result_file = "results/analysis_report.txt"

    firewall_status = check_firewall_status()
    ssh_root_status = check_ssh_root_login()

    results = [firewall_status, ssh_root_status]
    save_compliance_report(results, result_file)

    print("✅ Security compliance check complete. Results appended to the report.")

if __name__ == "__main__":
    main()
