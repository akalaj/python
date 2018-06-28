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

##########
###Main###
##########
#print getFirstName()
#print getMiddleInital()

for name in range(0, 1000000):
	print getFirstName() + " " + getMiddleInital() + " " + getLastName()