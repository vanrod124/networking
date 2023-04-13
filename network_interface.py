import psutil

def get_network_interfaces():
    interfaces = psutil.net_if_addrs()
    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                print(f"{interface}: {addr.address}")

get_network_interfaces()
