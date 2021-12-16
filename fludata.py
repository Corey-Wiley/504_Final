#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 21:56:54 2021

@author: coreywiley
"""

import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine


import pymysql

MYSQL_HOSTNAME = '40.117.74.71'
MYSQL_USER = 'dba'
MYSQL_PASSWORD = 'ahi2021'
MYSQL_DATABASE = 'e2e'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3306/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

print (engine.table_names())

fludata = pd.read_csv('/Users/coreywiley/Desktop/GRAD_AHI/504/H1N1_Flu_Vaccines.csv')

fludata.to_sql('fludata', con=engine, if_exists='append')