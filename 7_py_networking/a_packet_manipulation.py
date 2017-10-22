'Packet Manipulation with Scapy'

# Dummies Guide to Scapy
# https://theitgeekchronicles.files.wordpress.com/2012/05/scapyguide1.pdf


# On Mac brew install libdnet
# brew install libpcap


#-------------Important ----------
# launch subline with sudo subl . as we need admin privledges to run this.
# run sudo wireshark from terminal to launch wireshark
# display filter ip.addr == 'ip from your config file'

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from sejam_python_bootcamp import config
from scapy.all import *

dst = config.DESTINATION_IP

# fire up wireshark
#create and send single ICMP Packet
send(IP(dst=dst, ttl=64 )/ICMP()/"HelloWorld")
send(IP(dst=dst, ttl=128)/ICMP()/"HelloWorld")

# send single tcp packet to port 22.
sr1(IP(dst=dst)/TCP(dport=22))

# SYN Scan - Simple port scanner
answered, unanswered = sr(IP(dst=dst)/TCP(sport=666,dport=[22,8080,4118], flags='S'))

print('-----------------------------------------------------------------------------------------------------------------')
answered.summary()
print('-----------------------------------------------------------------------------------------------------------------')

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
for s,r in answered:
	print("S: %s:%s -> %s:%s\tR: %s:%s -> %s:%s" %( str(s[IP].src), str(s[IP].sport), str(s[IP].dst), str(s[TCP].dport),\
											   str(r[IP].src), str(r[IP].sport), str(r[IP].dst), str(r[TCP].dport)) )
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')