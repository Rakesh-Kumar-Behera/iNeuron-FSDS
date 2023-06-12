import mysql.connector
#
mydb = mysql.connector.connect(
  host="localhost", #127.0.0.1
  user="abc",
  password="password"
)

cur = mydb.cursor()

#cur.execute("use fsds_db")

cur.execute('select * from fsds_db.fsds1') #it returs a collection of tuples

for i in cur:
    print(i)