import scapy.all as scapy

def sniff(interface) :
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packets) :
    print(packets)


sniff("wlp2s0")

