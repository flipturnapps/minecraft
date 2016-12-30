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
	# thread.start_new_thread( killer, (p,"stuff") )
	thread.start_new_thread( inputter, (p,1) )
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

			
def inputter(p,num):
	while 1:
		inddd = raw_input()
		print inddd
		p.communicate(input=inddd)
print "hello world"

os.chdir("yold-bukkit")
run("java -jar craftbukkit.jar")
print "done"





