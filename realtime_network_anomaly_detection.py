import os
import pcapy
from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.l2 import Ether

def process_packet(packet):
    scapy_packet = Ether(packet)
    
    # Extract features from the captured packet
    if scapy_packet.haslayer(IP):
        ip_src = scapy_packet[IP].src
        ip_dst = scapy_packet[IP].dst
        proto = None

        if scapy_packet.haslayer(TCP):
            proto = "TCP"
            sport = scapy_packet[TCP].sport
            dport = scapy_packet[TCP].dport
        elif scapy_packet.haslayer(UDP):
            proto = "UDP"
            sport = scapy_packet[UDP].sport
            dport = scapy_packet[UDP].dport

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

    # Check if the interface is available
    devices = pcapy.findalldevs()
    if wifi_iface not in devices:
        print(f"Interface '{wifi_iface}' not found.")
        return

    # Start capturing packets
    cap = pcapy.open_live(wifi_iface, 65536, 1, 0)
    while True:
        header, packet = cap.next()
        process_packet(packet)

if __name__ == "__main__":
    main()
