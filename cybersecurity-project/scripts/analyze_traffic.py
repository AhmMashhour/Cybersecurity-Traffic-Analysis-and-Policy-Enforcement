import os

def analyze_logs(log_file_path):
    suspicious_keywords = ["error", "unauthorized", "failed", "denied"]
    findings = []

    with open(log_file_path, 'r', errors='ignore') as f:
        lines = f.readlines()
        for line in lines:
            if any(keyword in line.lower() for keyword in suspicious_keywords):
                findings.append(line.strip())

    return findings

def save_findings(findings, output_file):
    with open(output_file, 'a') as f:
        f.write("\n\n--- Log Analysis Findings ---\n")
        for item in findings:
            f.write(f"{item}\n")

def main():
    log_file = "logs/system_logs.log"
    result_file = "results/analysis_report.txt"

    if not os.path.exists(log_file):
        print(f"Error: '{log_file}' does not exist. Please place your log file first.")
        return

    findings = analyze_logs(log_file)
    save_findings(findings, result_file)

    print(f"✅ Log analysis completed. Findings appended to {result_file}")

if __name__ == "__main__":
    main()
