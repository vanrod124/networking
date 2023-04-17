from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP

def process_packet(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = None

        if packet.haslayer(TCP):
            proto = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif packet.haslayer(UDP):
            proto = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport

        if proto:
            # Extract more features if needed and process them
            print(f"{ip_src}:{sport} -> {ip_dst}:{dport} [{proto}]")

def main():
    # Find the name of your WiFi interface
    if os.name == "posix":
        wifi_iface = "en0"  # For macOS, replace this with your interface name
    elif os.name == "nt":
        wifi_iface = "Wi-Fi"  # For Windows, replace this with your interface name
    else:
        print("OS not supported")
        return

    # Start capturing packets
    sniff(iface=wifi_iface, prn=process_packet, store=0)

if __name__ == "__main__":
    main()
