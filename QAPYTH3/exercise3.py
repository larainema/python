#!/usr/bin/python3
import os, glob

homepath = os.environ['HOME']
print(homepath)

filenames = glob.glob(homepath, '**', True)
