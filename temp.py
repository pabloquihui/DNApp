# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import io
import sys
import subprocess

cmd = 'python DNApp3.py'
p = subprocess.Popen(cmd, shell = True)
out, err = p.communicate()
#print(err,out)
