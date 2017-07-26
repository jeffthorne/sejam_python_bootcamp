'Packet Manipulation with Scapy'

# Dummies Guide to Scapy
# https://theitgeekchronicles.files.wordpress.com/2012/05/scapyguide1.pdf

from scapy.all import *
# On Mac brew install libdnet
# brew install libpcap


dst = '34.207.103.140'

# fire up wireshark
#create and send single ICMP Packet
send(IP(dst=dst, ttl=64 )/ICMP()/"HelloWorld")
send(IP(dst=dst, ttl=128)/ICMP()/"HelloWorld")

# send single tcp packet to port 22.
sr1(IP(dst=dst)/TCP(dport=22))

# SYN Scan - Simple port scanner
answered, unanswered = sr(IP(dst=dst)/TCP(sport=666,dport= list(range(20,50)), flags='S'))

print('-----------------------------------------------------------------------------------------------------------------')
answered.summary()
print('-----------------------------------------------------------------------------------------------------------------')

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
for s,r in answered:
	print("S: %s:%s -> %s:%s\tR: %s:%s -> %s:%s" %( str(s[IP].src), str(s[IP].sport), str(s[IP].dst), str(s[TCP].dport),\
											   str(r[IP].src), str(r[IP].sport), str(r[IP].dst), str(r[TCP].dport)) )
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')