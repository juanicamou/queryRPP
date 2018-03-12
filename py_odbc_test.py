#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyodbc import *

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 11 for SQL Server};'
    r'SERVER=test;'
    r'DATABASE=test;'
    r'UID=user;'
    r'PWD=password'
    )

cursor = cnxn.cursor()

cursor.execute(#####Consulta#####)
row = cursor.fetchone()
if row:
    print(row)
cnxn.close()

#https://github.com/mkleehammer/pyodbc/wiki/Getting-started
