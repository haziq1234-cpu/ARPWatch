from collections import defaultdict

announcement_counts = defaultdict(int)

def check_arp(sender_ip, target_ip):
    if sender_ip == target_ip:
        announcement_counts[sender_ip] += 1

        print("[INFO] Gratuitous ARP detected")
        print("IP:", sender_ip)
        print("Count:", announcement_counts[sender_ip])
    else:
        print("[OK] Normal ARP observation")

# Dummy tests
check_arp("192.168.56.101", "192.168.56.102")
check_arp("192.168.56.101", "192.168.56.101")
check_arp("192.168.56.101", "192.168.56.101")
