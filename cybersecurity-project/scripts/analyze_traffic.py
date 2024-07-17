from scapy.all import rdpcap, TCP, IP

packets = rdpcap('pcap/capture_all.pcap')
for pkt in packets:
    if pkt.haslayer(TCP):
        print(f"Source: {pkt[IP].src}, Destination: {pkt[IP].dst}, Protocol: TCP, Length: {len(pkt)}")
