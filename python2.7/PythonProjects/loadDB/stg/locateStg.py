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

locations = Table('locations', metadata,
     Column('id', Integer, primary_key=True, autoincrement=True),
     Column('city', VARCHAR(50)),
     Column('code', CHAR(2)),
     Column('zip', Integer),
     mysql_engine='InnoDB',
     mysql_charset='utf8mb4'
)

###############
###Functions###
###############
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
	print "%s,%s %s" % (result_lo[1],result_lo[2], result_lo[0])


#emailChoice()

getLocation()