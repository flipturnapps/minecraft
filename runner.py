#!/usr/bin/python

import subprocess
import shlex
import os
import time
import thread

timelimit = .6*60*1000
warnlimit = .1*60*1000
shouldPrint = False

def currtime():
    return int(round(time.time() * 1000))
def run(exe):   
	p = subprocess.Popen(shlex.split(exe), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	print "running:  " + exe
	thread.start_new_thread( killer, (p,"stuff") )
	shouldPrint = True
	while shouldPrint:
		try:
			line = p.stdout.readline()
		except ValueError:
			break
		time.sleep(.001)
		if line != '':
			print line.rstrip()
		else:
			break

def killer(p,word):
	ct = currtime()
	warned = False
	while True:
		ct2 = currtime()
		if (warned != True and (ct2-ct) > (timelimit - warnlimit)):
			p.communicate(input='say Server will shutdown in one minute')
			warned = True
			print "warned"
		if ((ct2 - ct) > timelimit):
			p.communicate(input='stop')
			print "stopped"
			break

print "hello world"

os.chdir("yold-bukkit")
run("java -jar craftbukkit.jar")

print "done"





