#!/usr/bin/python3
import sys, os, glob

if sys.platform == 'win32':
   homepath = os.environ['HOMEPATH']
else:
   homepath = os.environ['HOME']
print(homepath)

pattern = os.path.join(homepath, '*')
print(pattern)

filenames = glob.glob(pattern)
print(filenames)

for filename in filenames:
    size = os.path.getsize(filename)
    #print(size)
    if size > 0:
       print('File:', os.path.basename(filename))
       print('Size:', size, 'bytes')
