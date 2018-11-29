#!/usr/bin/python2.7

###############
###CHALLENGE###
###############

'''
~DESCRIPTION~
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line
'''

#Variables
foundValues = []

#Opening Message
print "Finding all numbers between 2000 & 3200, divisble by 7 and not a multiple of 5"

#"For numbers between 2000->3200, see if it's divisble by 7, if so...divide 5 into and see if the remainder is > 0"
#If > than 0 then keep it....else...pass(fahget-aboutit)
for number in range(2000, 3200):
	if (number % 7 == 0) and (number % 5 != 0):
		foundValues.append(str(number))
		
print ','.join(foundValues)