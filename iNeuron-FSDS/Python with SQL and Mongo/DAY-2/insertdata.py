import mysql.connector

mydb = mysql.connector.connect(
  host="localhost", #127.0.0.1
  user="abc",
  password="password"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("""insert into ineuron.fsds values(123 , 'Rakesh' , 'Behera' , '2023-11-11' , 'sql' , 'fsds') ,
 (124 , 'Yash' , 'Behera' , '2023-01-18' , 'sql' , 'fsds'), 
 (125 , 'Nachi' , 'Dhal' , '2023-02-13' , 'sql' , 'fsds') , 
 (126 , 'Abhi' , 'Nayak' , '2023-11-15' , 'sql' , 'fsds'),
 (127 , 'Satya' , 'Patra' , '2023-05-18' , 'sql' , 'fsds'), 
 (128 , 'Shiba' , 'Mallik' , '2023-03-12' , 'sql' , 'fsds'), 
 (129 , 'Aditya' , 'Mahanty' , '2023-04-13' , 'sql' , 'fsds') , 
 (130 , 'Amit' , 'Tripathi' , '2023-11-15' , 'sql' , 'fsds'),
 (131 , 'Ritwick' , 'Mishra' , '2023-01-18' , 'sql' , 'fsds')
  """)

mydb.commit()

mycursor.execute("select * from ineuron.fsds")

for i in mycursor:
    print(i)