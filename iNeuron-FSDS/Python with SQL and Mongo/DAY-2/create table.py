import mysql.connector

mydb = mysql.connector.connect(
  host="localhost", #127.0.0.1
  user="abc",
  password="password"
)

print(mydb)

mycursor = mydb.cursor()


mycursor.execute('create table ineuron.fsds(studentid int , first_name varchar(50), last_name varchar(50),registration_date DATE , class varchar(20),course_name varchar(50))')