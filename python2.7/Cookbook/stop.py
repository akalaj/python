#!/usr/bin/python2.7

import threading
import time

#!/usr/bin/python2.7

def myfunc(i):
	for r in range(1, 8):
		time.sleep(1)
		print "Thread: %s Cycle: %s\n" % (i, r)


a = threading.Thread(target=myfunc, args=("a"))
a.start()

time.sleep(5.0)

a