import mysql.connector
database = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'Mysql'
)

cursor = database.cursor()
cursor.execute("create database elderco")
print("done")