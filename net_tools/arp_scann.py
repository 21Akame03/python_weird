import scapy.all as scapy
import optparse


def getArgs() :
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target/IP - IP range")
    (options, arguments) = parser.parse_args()
    return options


def findIP(ip) :
    # create a request object and send general arp request  
    arp_request = scapy.ARP(pdst=ip) 
    
    # using the bradcast mac address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast/arp_request
    
    # show the information about the packet
    print(f"\n################ arp packet #########################")
    arp_broadcast.show()
    
    # send and receive packet
    answered_list = scapy.srp(arp_broadcast, timeout=1)[0]
    
    # print the data 
    print(f"\n################ Arp response ########################")
    for data in answered_list:
        print(data[1].show())

        
options = getArgs()
findIP(options.target)
#  findIP("192.168.0.106/24")
