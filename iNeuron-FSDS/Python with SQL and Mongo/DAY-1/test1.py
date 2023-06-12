import mysql.connector
#
mydb = mysql.connector.connect(
  host="localhost", #127.0.0.1
  user="abc",
  password="password"
)

cur = mydb.cursor(())

#cur.execute("create database fsds_db")

cur.execute("use fsds_db")

#cur.execute("create table fsds1(name varchar(40) , roll_no int, nail_id varchar(50))")

cur.execute("insert into fsds1 values('Abhi' , 2255 , 'abhi@gmail.com')")

#cur.execute('select * from fsds1')

mydb.commit()