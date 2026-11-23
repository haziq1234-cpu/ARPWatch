from scapy.all import sniff, ARP

def packet_handler(packet):
    if ARP in packet:
        arp = packet[ARP]

        print(
            "ARP Packet | "
            "Operation:", arp.op,
            "| Sender IP:", arp.psrc,
            "| Sender MAC:", arp.hwsrc
        )

sniff(
    filter="arp",
    prn=packet_handler,
    store=False
)
