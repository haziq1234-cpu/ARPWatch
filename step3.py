ip_mac_table = {}

def check_mac(ip, mac):
    if ip not in ip_mac_table:
        ip_mac_table[ip] = mac
        print(f"[INFO] New device: {ip} -> {mac}")

    elif ip_mac_table[ip] == mac:
        print(f"[OK] Mapping unchanged: {ip} -> {mac}")


    else:
        old_mac = ip_mac_table[ip]
        print("[ALERT] MAC address changed!")
        print(f"IP: {ip}")
        print(f"Old MAC: {old_mac}")
        print(f"New MAC: {mac}")

        ip_mac_table[ip] = mac


# Test data
check_mac("192.168.56.102", "AA:BB:CC:11:22:44")
check_mac("192.168.56.102", "AA:BB:CC:11:22:44")
check_mac("192.168.56.102", "DD:EE:FF:11:22:44")
