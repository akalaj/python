#!/usr/bin/python2.7

#vars
value = raw_input("Please provide input to be latin'ed\n")
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
global finalProduct

#funcs
def latinize(phrase):
	finalProduct = ""
	for word in phrase.split(" "):
		found = 0
		keepWord = ""
		move = []
		keep = []
		for letter in list("%s" % word):
			if letter in consonants:
				if len(move) >= 1:
					keep.append("%s" % letter)
				else:
					move.append("%s" % letter)
			else:
				keep.append("%s" % letter)
		for st1 in keep:
			keepWord += st1
		for st2 in move:
			keepWord += st2
		keepWord += "ay"
		finalProduct += keepWord + " "
	print finalProduct

#main (lol)
latinize(value)