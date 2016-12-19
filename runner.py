#!/usr/bin/python

import subprocess
import shlex
import os
import time
import thread

timelimit = 3*60*1000
warnlimit = 1*60*1000
shouldPrint = False

def currtime():
    return int(round(time.time() * 1000))
def run(exe):   
	p = subprocess.Popen(shlex.split(exe), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	print "running:  " + exe
	thread.start_new_thread( killer, (p,"stuff") )
	shouldPrint = True
	while (shouldPrint==True):
		try:
			line = p.stdout.readline()
		except ValueError:
			break
		time.sleep(.1)
		if line != '':
			print line.rstrip()
		else:
			break

def killer(p,word):
	ct = currtime()
	warned = 0
	stopped = 0
	while True:
		time.sleep(.1)
		ct2 = currtime()
		if (warned == 0 and (ct2-ct) > (timelimit - warnlimit)):
			p.communicate(input='say Server will shutdown in one minute')
			warned = 1
			print "warned"
		if (stopped == 0 and (ct2 - ct) > timelimit):
			p.communicate(input='stop')
			print "stopped"
			shouldPrint = False
			stopped = 1
			break

print "hello world"

os.chdir("yold-bukkit")
run("java -jar craftbukkit.jar")

print "done"





