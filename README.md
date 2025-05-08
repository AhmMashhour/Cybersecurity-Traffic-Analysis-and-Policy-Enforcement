# Cybersecurity Traffic Analysis and Policy Enforcement

## Project Overview

This project is a Cybersecurity Traffic Analysis and Policy Enforcement focused on capturing and analyzing network traffic. Utilizing advanced tools such as tcpdump, Wireshark, Scapy, and Volatility, this project aims to monitor network activities, conduct digital forensic analysis, and develop robust security policies through Python and Ansible.


## Directory Structure

cybersecurity-project/

├── scripts/ # Python scripts for traffic and system analysis

├── pcap/ # Directory for captured network traffic files

├── logs/ # Directory for system log files

├── ansible/ # Ansible playbook for security policy enforcement

└── results/ # Analysis results and findings


## Technologies Used

- **tcpdump**: For capturing network traffic.
- **Wireshark**: For analyzing captured packet data.
- **Scapy**: A Python library used for packet manipulation and analysis.
- **Volatility**: A tool for memory forensics.
- **Python**: For scripting and automation tasks.
- **Ansible**: For configuration management and enforcing security policies.


### Setup Instructions

1. **Capture Network Traffic:**
   Execute the following command to capture network traffic:
   ```bash
   sudo tcpdump -i eth0 -nn -c 1000 -w pcap/capture_all.pcap
   
2. **Analyze Network Traffic:**
   Open the "capture_all.pcap" file in Wireshark.
   Apply filters to focus on HTTP and HTTPS traffic

3. **Run Python Analysis Scripts:**
   Execute the following command to analyze traffic data:
   ```bash
   python3 scripts/analyze_traffic.py

4. **Conduct Memory Analysis:**
   Use Volatility to analyze memory images:
   ```bash
   volatility -f mem_dump.raw --profile=WinXPSP2x86 pslist

5. **Enforce Security Policies with Ansible:**
   Run the following command to enforce security policies:
   ```bash
   ansible-playbook ansible/security_policies.yml


## Results
- Packet Analysis: Successfully captured and analyzed network traffic, identifying suspicious connections for further investigation.
- Digital Forensic Analysis: Conducted thorough memory and log analysis to uncover potential security incidents.
- Security Policies: Developed compliance verification scripts and implemented network-wide policies using Ansible.


## Conclusion
This project showcases a holistic approach to cybersecurity, demonstrating expertise in network monitoring, forensic analysis, and security policy implementation. It serves as a valuable asset for any cybersecurity professional's portfolio.


## Acknowledgments
Special thanks to the open-source community for the tools and resources utilized in this project
