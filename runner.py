#!/usr/bin/python

import subprocess
import shlex
import os
def run(exe):  
    print "running"  
    p = subprocess.Popen(shlex.split(exe), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print "running" + exe
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()


print "hello world"

#run("cd yold-bukkit")
os.chdir("yold-bukkit")
run("ls")

print "done"





