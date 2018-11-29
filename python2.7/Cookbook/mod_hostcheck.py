#!/usr/bin/python2.7

import threading
import time
import os
import subprocess
from subprocess import Popen,PIPE

#Thread object to perform MySQL check
class mysqlCheckThread(threading.Thread):

	def __init__(self, name='mysqlCheckThread'):
		""" constructor, setting initial variables """
		self._stopevent = threading.Event()
		self._sleepperiod = 1.0

		threading.Thread.__init__(self, name=name)

	def run(self):
		""" MySQL Check """

		count = 0
		while not self._stopevent.isSet():
			print "loop %d" % (count,)
			mysqlAdminCheck = Popen("/usr/bin/mysqladmin -uroot -p%s -h%s -P3306 ping" % (password,hostname),shell=True,stdout=PIPE,stderr=PIPE)
			(out,err) = mysqlAdminCheck.communicate()
			if mysqlAdminCheck.returncode != 1:
				#MySQL Admin Check Failed
				print "%s: MySQL is running" % hostname
			else:
				print "%s: MySQL is NOT running" % hostname


		print "%s ends" % (self.getName(),)

	def join(self, timeout=None):
		""" Stop the thread. """
		self._stopevent.set()
		threading.Thread.join(self, timeout)

if __name__ == "__main__":

	#Read hostfile to determmine hosts to check
	file = open("./list.txt", "r").read().splitlines()

	#creds
	mysql_pass = "s2mMdPpckC"

	#Create a thread and check MySQL
	for hostname in file:
		CheckThread = mysqlCheckThread()
		CheckThread.start()
		time.sleep(5.0)
		mysqlCheckThread.join()