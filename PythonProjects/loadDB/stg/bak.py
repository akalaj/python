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
decsion = ["single", "number", "dot", "underscore"]

#Table Definitions for use in sqlalchemy/mysql queries

words = Table('words', metadata,
     Column('id', Integer, primary_key=True, autoincrement=True),
     Column('word', CHAR(1)),
     mysql_engine='InnoDB',
     mysql_charset='utf8'
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



##########
###Main###
##########

print getEmail()