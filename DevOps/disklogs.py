#!/usr/bin/env python
#!coding=utf-8

import time
import os

new_time = time.strftime('%Y-%m-%d')
disk_status = os.popen('df -h').readlines()
print(disk_status)
str = ''.join(disk_status)
f = open(new_time + '.log', 'w')
f.write('%s' % str)
f.flush()
f.close()
