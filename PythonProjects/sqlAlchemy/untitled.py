import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.sql import select
from sqlalchemy.sql import text

db_uri = "mysql://admin:mypass@127.0.0.1:3306/customers"

#Create SQL Alchemy Engine using MySQL connection string
engine = create_engine(db_uri, connect_args={'connect_timeout': 60})

#Connect using the engine object
conn = engine.connect()

#fname id
fId = "50"

#Start a transaction
trans = conn.begin()

#The "MetaData" object is actually a Python Dictionary.
#It holds meta info on what connections and schema related things
#are taking place.
meta = MetaData(engine)

#customerTbl = Table('users', meta,
#   Column('id', Integer, primary_key=True),
#   Column('fname', String(50)),
#   Column('lname', String(50)),
#   Column('email', String(50))
#)

fnameTbl = Table('fnames', meta,
   Column('id', Integer, primary_key=True),
   Column('fname', String(50))
)

fnameQuery = select([fnameTbl]).where(text("id = %s" % fId))


result = conn.execute(fnameQuery).fetchone()

print result[1]