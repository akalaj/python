import random

def getEmail():
    p = random.choice([1,2,3,4])
    if p == 1:
    	print "single!"
    if p == 2:
    	print "number!"
    if p == 3:
    	print "dot!"
    if p == 4:
    	print "underscore"

getEmail()
