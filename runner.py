#!/usr/bin/python

import subprocess
import shlex
import os
import time

def currtime():
    return int(round(time.time() * 1000))
def run(exe):   
    p = subprocess.Popen(shlex.split(exe), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print "running:  " + exe
    ct = currtime()
    while True:
        line = p.stdout.readline()
        time.sleep(.01)
        if line != '':
            print line.rstrip()
            ct2 = currtime()
            if ((ct2 - ct) > 20000):
				print "stoo"
				p.communicate(input='stop')
        else:
            break


print "hello world"

#run("cd yold-bukkit")
os.chdir("yold-bukkit")
run("java -jar craftbukkit.jar")

print "done"





