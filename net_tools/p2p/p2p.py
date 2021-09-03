import pyp2p.net as p2p
import time as time

# Setup Alice's p2p node 
alice = p2p.Net(passive_bind="192.168.0.48", passive_port=4444, interface="wlp2s0:2", node_type="passive", debug=1)
alice.start()
alice.bootstrap()
alice.advertise()


#event loop
while i :
    for con in alice:
        for reply in con:
            print(reply)

        time.sleep(1)
