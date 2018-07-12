# -*- coding: UTF-8 -*-
import os,sys,re
#https://www.cnblogs.com/darkpig/p/7627080.html
#scapy win 下有毛病fuck
from scapy.all import *
list = []

arplist = os.system("arp -d")

for i in range(1,253,1):
    list.append(i)
    ip = "103.1.8."+str(i)
    print(ip)
    os.system("ping -n 1 "+ip)


output = os.popen('arp -a')
arplist = output.read()
result = re.findall(r'.*2c-27-d7-3c-b5-65.*',arplist)
print(result)