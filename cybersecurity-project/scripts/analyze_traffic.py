import scapy.all as scapy
import os

def read_pcap(file_path):
    packets = scapy.rdpcap(file_path)
    return packets

def analyze_packets(packets):
    http_traffic = 0
    https_traffic = 0
    suspicious_ips = set()

    for pkt in packets:
        if pkt.haslayer(scapy.IP):
            ip_layer = pkt[scapy.IP]
            if ip_layer.dport == 80:
                http_traffic += 1
            elif ip_layer.dport == 443:
                https_traffic += 1
            if ip_layer.dst not in ['8.8.8.8', '1.1.1.1']:  # suspicious if not to common DNS
                suspicious_ips.add(ip_layer.dst)

    return http_traffic, https_traffic, suspicious_ips

def save_results(http, https, suspects, output_file):
    with open(output_file, 'w') as f:
        f.write(f"HTTP Requests: {http}\n")
        f.write(f"HTTPS Requests: {https}\n")
        f.write("Suspicious IPs:\n")
        for ip in suspects:
            f.write(f"{ip}\n")

def main():
    pcap_file = "pcap/capture_all.pcap"
    result_file = "results/analysis_report.txt"

    if not os.path.exists(pcap_file):
        print(f"PCAP file '{pcap_file}' not found.")
        return

    packets = read_pcap(pcap_file)
    http, https, suspects = analyze_packets(packets)
    save_results(http, https, suspects, result_file)

    print(f"Analysis complete. Results saved to {result_file}.")

if __name__ == "__main__":
    main()
