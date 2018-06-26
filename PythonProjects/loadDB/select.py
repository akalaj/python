#!/usr/bin/python2.7

import random
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.sql import select
from sqlalchemy.sql import text

#############
###Classes###
#############

#class newCustomer:
#	def __init__(self, cFirstName, cMiddleInital, cLastName):
#		self.cFirstName = cFirstName
#		self.cMiddleInital = cMiddleInital
#		self.cLastName = cLastName
		


###############
###Functions###
###############

#def dbConnect():
#	#Connection String
#	db_uri = "mysql://admin:mypass@127.0.0.1:3306/customers"
#
#	#build engine
#	engine = create_engine(db_uri, connect_args={'connect_timeout': 60})
#
#	#create database meta engine
#	meta = MetaData(engine)


def readFnames():

	#Connect using the engine object
	conn = engine.connect()

	#Start a transaction
	trans = conn.begin()

	#build sqlalchemy query structure
	readQuery = select([fnames]).where(text("id = %s" % fnamesId))

	#Execute assembled query and assign object to "result"
	result = conn.execute(readQuery).fetchone()

	#return the result of the first name query
	return result[1]

###############
###Variables###
###############

#Randomly assembled user ids based on fixed number of values inside corresponding tables
#fnamesId = random.randrange(1, 1219)
#lnamesId = random.randrange(1, 1000)
#initalId = random.randrange(1, 26)
#
##MySQL Table definitions for use with sqlalchemy
#fnames = Table('fnames', meta,
#   Column('id', Integer, primary_key=True),
#   Column('fname', String(50))
#)


##########
###Main###
##########

def main():
	db_uri = "mysql://admin:mypass@127.0.0.1:3306/customers"
	engine = create_engine(db_uri, connect_args={'connect_timeout': 60})
	meta = MetaData(engine)

	#Randomly assembled user ids based on fixed number of values inside corresponding tables
	fnamesId = random.randrange(1, 1219)
	lnamesId = random.randrange(1, 1000)
	initalId = random.randrange(1, 26)
	
	#MySQL Table definitions for use with sqlalchemy
	fnames = Table('fnames', meta,
	   Column('id', Integer, primary_key=True),
	   Column('fname', String(50))
	)

	readFnames()

main()