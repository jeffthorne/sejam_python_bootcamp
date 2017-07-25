from scapy.all import *

# On Mac brew install libdnet
# Dummies Guide to Scapy

send(IP(dst=b"34.207.103.140")/ICMP()/b"HelloWorld")