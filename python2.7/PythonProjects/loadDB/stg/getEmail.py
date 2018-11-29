#!/usr/bin/python

'''
Reach into MySQL and see if we can obtain the results we'll need for building a fictional customer database.
'''

##############
###Packages###
##############
import random
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR, CHAR
from sqlalchemy.sql import select, func

###############
###Variables###
###############
db_uri = "mysql://alchemy:sqlpass@sql.com:3306/customers"
engine = create_engine(db_uri)
conn = engine.connect()
trans = conn.begin()
metadata = MetaData()

#Logical supplements
decision = ["single", "number", "dot", "underscore"]

#Table Definitions for use in sqlalchemy/mysql queries

words = Table('words', metadata,
     Column('id', Integer, primary_key=True, autoincrement=True),
     Column('word', CHAR(1)),
     mysql_engine='InnoDB',
     mysql_charset='utf8mb4'
)

emailProviders = Table('emailProviders', metadata,
     Column('id', Integer, primary_key=True, autoincrement=True),
     Column('provider', CHAR(15)),
     mysql_engine='InnoDB',
     mysql_charset='utf8mb4'
)

###############
###Functions###
###############
def getEmail():
	#get max id
	max_wid = select([func.max(words.c.id).label('max_id')])
	found_wid = conn.execute(max_wid)
	result_wid = found_wid.fetchone()
	#retrieve firstname (lname)
	pkid = random.randrange(1, result_wid[0])
	query_word = select([words.c.word]).where(words.c.id == pkid)
	found_word = conn.execute(query_word)
	result_word = found_word.fetchone()
	#return results
	return result_word[0]

def getProvider():
	#get max id
	max_epid = select([func.max(emailProviders.c.id).label('max_id')])
	found_epid = conn.execute(max_epid)
	result_epid = found_epid.fetchone()
	#retrieve firstname (lname)
	pkid = random.randrange(1, result_epid[0])
	query_word = select([emailProviders.c.provider]).where(emailProviders.c.id == pkid)
	found_word = conn.execute(query_word)
	result_word = found_word.fetchone()
	#return results
	return result_word[0]


##########
###Main###
##########

def emailChoice():
    p = random.choice([1,2,3,4])
    if p == 1:
    	email = getEmail()
    	provider = getProvider()
    	print str(email+"@"+provider)
    if p == 2:
    	email = getEmail()+str(random.randrange(1,7777))
    	provider = getProvider()
    	print str(email+"@"+provider)
    if p == 3:
    	email = getEmail()+"."+getEmail()
    	provider = getProvider()
    	print str(email+"@"+provider)
    if p == 4:
    	email = getEmail()+"_"+getEmail()
    	provider = getProvider()
    	print str(email+"@"+provider)


#emailChoice()

emailChoice()