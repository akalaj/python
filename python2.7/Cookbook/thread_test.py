#!/usr/bin/python2.7

import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.sql import select

print sys.argv[1]

pip install MySql-Python
pip install SQLAlchemy