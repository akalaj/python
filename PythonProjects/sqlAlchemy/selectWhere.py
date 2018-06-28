#!/usr/bin/python

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.sql import select

#MySQL Connection string
#uri = 'mysql://$USERNAME:$PASSWORD@$HOST:$PORT/'
db_uri = "mysql://alchemy:sqlpass@sql.com:3306/alchemy"

#Create SQL Alchemy Engine using MySQL connection string
engine = create_engine(db_uri)

#Connect using the engine object
conn = engine.connect()

#Start a transaction
trans = conn.begin()

#Create a MySQL metaData dictionary to hold information about the table we're writing to
metadata = MetaData()

#Describe to sqlalchemy the table we're writing to. We'll generate this table object using the "import Table" package we imported earlier 
users = Table('users', metadata,
     Column('id', Integer, primary_key=True, autoincrement=True),
     Column('name', VARCHAR(45, collation='utf8mb4_general_ci')),
     Column('fullname', VARCHAR(45, collation='utf8mb4_general_ci')),
     mysql_engine='InnoDB',
     mysql_charset='utf8mb4',
     mysql_row_format='COMPRESSED'
)

#using the package "select" that is mentioned in our above import statement
#create a "cursor" that will select values from a table matching our table object
s = select([users]).where(users.c.id == 4)

#execute the select by using the cursor to reach into MySQL and store the found rows in a sqlalchemy rows object
result = conn.execute(s)

#close transaction we started earlier. Inserted values won't appear until transaction closes
trans.commit()

#close datbase connection
conn.close()

#Use a for loop to print the values in the "result" storage object
row = result.fetchone()

#print values
print row