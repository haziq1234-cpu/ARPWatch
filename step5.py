from collections import defaultdict

mac_ip_table = defaultdict(set)

def add_mapping(ip, mac):
    mac_ip_table[mac].add(ip)

def show_table():
    print("\n--- MAC TO IP TABLE ---")

    for mac, ips in mac_ip_table.items():
        print(f"MAC: {mac}")
        print(f"IPs: {', '.join(sorted(ips))}")
        print(f"Total IPs: {len(ips)}")

# Dummy test data
add_mapping("192.168.56.101", "AA:BB:CC:11:22:33")
add_mapping("192.168.56.102", "AA:BB:CC:11:22:33")
add_mapping("192.168.56.103", "DD:EE:FF:11:22:44")

show_table()
