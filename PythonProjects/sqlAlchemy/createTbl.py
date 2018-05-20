#!/usr/bin/python2.7

#########################################
###How To Create A Table In sqlAlchemy###
#########################################

'''
This is a small sample on how to create a table using sqlalchemy.
I created this script to help me and others remember the syntax for creating tables.

Question: "What is MetaData?"

MetaData is a dictionary that holds table structure information.

The below code will demonstrate how to populate the MetaData python dictionary
and add table structure information.

Once the MetaData dict is loaded with table structure data, we will
extract that value info and ship it as a query for MySQL to create.
'''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String

#MySQL Connection string
#uri = 'mysql://$USERNAME:$PASSWORD@$HOST:$PORT/'
#This connection string also has a timeout value of 120 seconds
db_uri = "mysql://alchemy:sqlalchemy@sql.com:3306/alchemy"

#Create SQL Alchemy Engine using MySQL connection string
engine = create_engine(db_uri, connect_args={'connect_timeout': 60})

#Connect using the engine object
conn = engine.connect()

#Start a transaction
trans = conn.begin()

#The "MetaData" object is actually a Python Dictionary.
#It holds meta info on what connections and schema related things
#are taking place.
meta = MetaData(engine)

##########################
###CREATE'ing the table###
##########################

'''
This was confusing when I first learned it so I've taken the liberty
of explaining some stuff that initially confused me.

With sqlalchemy, you must import your column type.
For example...

Notice how I imported Integer & String at the top.

For a complete list of data types you can use visit the URL below:
http://infohost.nmt.edu/~shipman/soft/sqlalchemy/web/column-types.html

Additionally, table create options must be added after column definitions.
As you can see in the example below, I've created 3 table options.
Typically, table options are prefixed with "mysql_"

For more table options see below:
http://docs.sqlalchemy.org/en/latest/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqldb
'''


table1 = Table('customersIII', meta,
           Column('id', Integer, primary_key=True),
           Column('name', String(30)),
           mysql_engine='InnoDB',
           mysql_charset='utf8mb4',
           mysql_row_format='compressed')
table1.create()

#close transaction we started earlier. Database connection closed in next step
trans.commit()

#close datbase connection
conn.close()