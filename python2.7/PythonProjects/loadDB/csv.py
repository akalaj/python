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
import sys

###############
###Variables###
###############
db_uri = "mysql://alchemy:sqlpass@sql.com:3306/customers"
engine = create_engine(db_uri)
conn = engine.connect()
metadata = MetaData()
instance = sys.argv[1]
filename = "insert%s.txt" % instance

dec = ["single", "number", "dot", "underscore"]

#Table Definitions for use in sqlalchemy/mysql queries
fnames = Table('fnames', metadata,
     Column('id', Integer, primary_key=True, autoincrement=True),
     Column('fname', VARCHAR(45)),
     mysql_engine='InnoDB',
     mysql_charset='utf8'
)

lnames = Table('lnames', metadata,
     Column('id', Integer, primary_key=True, autoincrement=True),
     Column('lname', VARCHAR(45)),
     mysql_engine='InnoDB',
     mysql_charset='utf8'
)

initals = Table('initals', metadata,
     Column('id', Integer, primary_key=True, autoincrement=True),
     Column('inital', CHAR(1)),
     mysql_engine='InnoDB',
     mysql_charset='utf8'
)

words = Table('words', metadata,
     Column('id', Integer, primary_key=True, autoincrement=True),
     Column('word', CHAR(1)),
     mysql_engine='InnoDB',
     mysql_charset='utf8'
)

emailProviders = Table('emailProviders', metadata,
     Column('id', Integer, primary_key=True, autoincrement=True),
     Column('provider', CHAR(15)),
     mysql_engine='InnoDB',
     mysql_charset='utf8mb4'
)

locations = Table('locations', metadata,
     Column('id', Integer, primary_key=True, autoincrement=True),
     Column('city', VARCHAR(50)),
     Column('code', CHAR(2)),
     Column('zip', Integer),
     mysql_engine='InnoDB',
     mysql_charset='utf8mb4'
)

customers = Table('customers', metadata,
     Column('id', Integer, primary_key=True, autoincrement=True),
     Column('firstname', VARCHAR(50)),
     Column('inital', CHAR(1)),
     Column('lastname', VARCHAR(50)),
     Column('email', VARCHAR(95)),
     Column('number', VARCHAR(12)),
     Column('city', VARCHAR(50)),
     Column('state', VARCHAR(2)),
     Column('zip', Integer),
     mysql_engine='InnoDB',
     mysql_charset='utf8mb4'
)

###############
###Functions###
###############
def getFirstName():
	#get max id
	max_fid = select([func.max(fnames.c.id).label('max_id')])
	found_id = conn.execute(max_fid)
	result_id = found_id.fetchone()
	#retrieve firstname (fname)
	pkid = random.randrange(1, result_id[0])
	query_fname = select([fnames.c.fname]).where(fnames.c.id == pkid)
	found_fname = conn.execute(query_fname)
	result_fname = found_fname.fetchone()
	#return results
	return result_fname[0]

def getMiddleInital():
	#get max id
	max_iid = select([func.max(initals.c.id).label('max_id')])
	found_iid = conn.execute(max_iid)
	result_iid = found_iid.fetchone()
	#retrieve firstname (fname)
	pkid = random.randrange(1, result_iid[0])
	query_inital = select([initals.c.inital]).where(initals.c.id == pkid)
	found_inital = conn.execute(query_inital)
	result_inital = found_inital.fetchone()
	return result_inital[0]

def getLastName():
	#get max id
	max_lid = select([func.max(lnames.c.id).label('max_id')])
	found_id = conn.execute(max_lid)
	result_id = found_id.fetchone()
	#retrieve firstname (lname)
	pkid = random.randrange(1, result_id[0])
	query_lname = select([lnames.c.lname]).where(lnames.c.id == pkid)
	found_lname = conn.execute(query_lname)
	result_lname = found_lname.fetchone()
	#return results
	return result_lname[0]

def getWord():
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



def emailChoice():
    p = random.choice([1,2,3,4])
    if p == 1:
    	email = getEmail()
    	provider = getProvider()
    	return str(email+"@"+provider)
    if p == 2:
    	email = getEmail()+str(random.randrange(1,7777))
    	provider = getProvider()
    	return str(email+"@"+provider)
    if p == 3:
    	email = getEmail()+"."+getEmail()
    	provider = getProvider()
    	return str(email+"@"+provider)
    if p == 4:
    	email = getEmail()+"_"+getEmail()
    	provider = getProvider()
    	return str(email+"@"+provider)

def getLocation():
	#get max id
	max_loid = select([func.max(locations.c.id).label('max_id')])
	found_loid = conn.execute(max_loid)
	result_loid = found_loid.fetchone()
	#retrieve firstname (lname)
	pkid = random.randrange(1, result_loid[0])
	query_lo = select(['*']).where(locations.c.id == pkid)
	found_lo = conn.execute(query_lo)
	result_lo = found_lo.fetchone()
	#return results
	location = "%s,%s,%s" % (result_lo[1],result_lo[2],result_lo[0])
	return location

##########
###Main###
##########

number = "4803144918"
quantity = 1000

insValues = {}

file = open(filename, "w")

for i in range(quantity):
	trans = conn.begin()
	insValues['firstname'] = getFirstName()
	insValues['inital'] = getMiddleInital()
	insValues['lastname'] = getLastName()
	insValues['email'] = emailChoice()
	location = getLocation().split(",")
	insValues['number'] = number
	insValues['city'] = location[0]
	insValues['state'] = location[1]
	insValues['zip'] = int(location[2])
	#INSERT
	STR = "\"%s\",\"%s\",\"%s\",\"%s\",%s,\"%s\",\"%s\",%s" % (insValues['firstname'],insValues['inital'],insValues['lastname'],insValues['email'],insValues['number'],insValues['city'],insValues['state'],insValues['zip'])
	file.write("%s\n" % STR)
	trans.commit()


