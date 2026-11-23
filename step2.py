ip_mac_table = {}

def add_device(ip, mac):
    ip_mac_table[ip] = mac

def show_table():
    print("\n--- IP MAC TABLE ---")
    for ip, mac in ip_mac_table.items():
        print(f"{ip}  ->  {mac}")
    print("-------------------")
