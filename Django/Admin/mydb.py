# install mysql 


import mysql.connector

database = mysql.connector.connect(
host= "localhost",
user = "root",
database = "IncomingUser",
passwd = "Password123",
)
cursorOBJ = database.cursor()
cursorOBJ.execute("CREATE DATABASE IncomingUser")
print("Database Created")