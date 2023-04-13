import socket
from scapy.all import ARP, Ether, srp
import time
from collections import deque

def get_local_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def arp_scan(ip_range):
    devices = []
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
    ans, _ = srp(arp_request, timeout=2, verbose=0)

    for _, response in ans:
        devices.append({
            'ip': response.psrc,
            'mac': response.hwsrc
        })

    return devices

def get_number_of_connected_devices():
    local_ip = get_local_ip()
    ip_range = local_ip + "/24"
    devices = arp_scan(ip_range)
    return len(devices)


def establish_baseline(window_size, interval):
    historical_data = deque(maxlen=window_size)

    for _ in range(window_size):
        num_devices = get_number_of_connected_devices()
        historical_data.append(num_devices)
        time.sleep(interval)

    avg_devices = sum(historical_data) / len(historical_data)
    threshold = avg_devices * 1.2  # You can adjust the threshold multiplier based on your needs

    return threshold

if __name__ == "__main__":
    window_size = 5  # Number of data points to consider in the baseline
    interval = 5  # Time interval between data collection (in seconds)
    threshold = establish_baseline(window_size, interval)
    print(f"Established threshold: {threshold}")
