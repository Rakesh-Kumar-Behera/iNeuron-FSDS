import mysql.connector

mydb = mysql.connector.connect(
  host="localhost", #127.0.0.1
  user="abc",
  password="password"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute('create database ineuron')