#root mysql password is "mysql"
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql"
)

mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE mydatabase")
mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
