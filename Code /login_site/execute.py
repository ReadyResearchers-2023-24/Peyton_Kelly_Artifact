'''Connect to SQL databases'''

# Import libraries

import pandas as pd
import numpy as np
import os
import sys


# Connect to SQL Server
def connect_to_sql_server():
    '''Connect to SQL Server'''
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-4QO0Q5M\SQLEXPRESS;'
                              'Database=AdventureWorks2017;'
                              'Trusted_Connection=yes;')
        print('Connected to SQL Server')
        return conn
    except:
        print('Error connecting to SQL Server')
        sys.exit(1)

#fuction to execute SQL query (ip address)
def execute_sql_query(conn, query):
    '''Execute SQL query'''
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        print('Query executed successfully')
        return cursor
    except:
        print('Error executing query')
        sys.exit(1) 