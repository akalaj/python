#!/usr/bin/python2.7

############################################
###How To Create A Database In sqlAlchemy###
############################################

'''
This is a small sample on how to create a database using sqlalchemy.
I created this script to help me and others remember the syntax for creating databases.
'''

import sqlalchemy
from sqlalchemy import create_engine

#MySQL Connection string
#uri = 'mysql://$USERNAME:$PASSWORD@$HOST:$PORT/'
db_uri = "mysql://alchemist:sqlalchemy@sql.com:3306/"

#Create SQL Alchemy Engine using MySQL connection string
engine = create_engine(db_uri)

#Connect using the engine object
conn = engine.connect()

#Start a transaction
trans = conn.begin()

#create database on the host specified in the connection string
conn.execute("CREATE DATABASE `alchemy`")

#close transaction we started earlier. Database connection closed in next step
trans.commit()

#close datbase connection
conn.close()