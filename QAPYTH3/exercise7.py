#!/usr/bin/python3
import re

f = open('/etc/services', 'r')

ports = set()

for line in f:
    if line.isspace(): continue
    if line[0] == '#': continue
    #print(line)
    m = re.search(r'(\d+)/(udp|tcp)', line)
    if m:
        #print(m)
        port = int(m.groups()[0])
        #print(port)
        if port > 200: break
        ports.add(port)

print(set(range(1,201)) - ports)   

f.close()     
