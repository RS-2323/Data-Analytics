"""
Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like Student_Name, Student_Age, 
Student_Roll_no, Student_Branch.
"""

import sqlite3
from pandas import DataFrame


# File based database ( connects if exists or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'student.db' )


# creating cursor
c = conn.cursor()

#Delete the table
c.execute("DROP TABLE students")
conn.commit()

# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE students(
          Student_Name TEXT,
          Student_Age  INT,
          Student_Roll_no BIGINT,
          Student_Branch TEXT
          )"""
          )
conn.commit()


# STEP 2
c.execute("INSERT INTO students VALUES ('Riya',18,180612017, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Sapna', 18,180612016,'MLAI')")
c.execute("INSERT INTO students VALUES ('Lakshya',18, 180612014, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Lavish',18,180612012, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Dushyant',18,180612007, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Ashwini',18, 180612011, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Ankit',18, 180612010, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Dinesh', 18,180612009, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Vishal', 18,180612006, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Shubham',18,18061205, 'MLAI')")
conn.commit()


# STEP 3
c.execute("SELECT * FROM students")
# "SELECT * FROM employees WHERE last = 'Fernandes' "



# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM students")


# STEP 5
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Student_Name","Student_Age","Student_Roll_no","Student_Branch"]
#df.to_csv("employee.csv")


# STEP 6
# closing the connection 
conn.close()


print ( c.fetchone()) 




"""
Database handling using MySQL on Cloud
"""
import mysql.connector 
# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='riyasharma', password='Bsdu@123',host='db4free.net', database = 'twitter_first')


# creating cursor
c = conn.cursor()
# STEP 0
#c.execute("DROP DATABASE employee;")

# STEP 1
#c.execute("CREATE DATABASE employee;")

# STEP 2
c.execute("DROP Table students;")

# STEP 3

c.execute ("""CREATE TABLE students(
          Student_Name TEXT,
          Student_Age  INT,
          Student_Roll_no BIGINT,
          Student_Branch TEXT
          )"""
          )
conn.commit()


# STEP 4
c.execute("INSERT INTO students VALUES ('Riya',18,180612017, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Sapna', 18,180612016,'MLAI')")
c.execute("INSERT INTO students VALUES ('Lakshya',18, 180612014, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Lavish',18,180612012, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Dushyant',18,180612007, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Ashwini',18, 180612011, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Ankit',18, 180612010, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Dinesh', 18,180612009, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Vishal', 18,180612006, 'MLAI')")
c.execute("INSERT INTO students VALUES ('Shubham',18,18061205, 'MLAI')")

conn.commit()

c.execute("SELECT * FROM students")


# STEP 5
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM student")


# STEP 6
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Student_Name","Student_Age","Student_Roll_no","Student_Branch"]

conn.close()

"""
Mongodb
"""
import pymongo


client = pymongo.MongoClient("mongodb+srv://riya_sharma:DX2KGYPvfYo5t3z5@cluster0-ahfv6.mongodb.net/test?retryWrites=true&w=majority")
mydb = client.forsk_db



def add_employee(idd, first, last, pay):
    unique_employee = mydb.forsk_coll.find_one({"id":idd})
    if unique_employee:
        return "Employee already exists"
    else:
        mydb.forsk_coll.insert_one(
                {
                "id" : idd,
                "first" : first,
                "last" : last,
                "pay" : pay
                })
        return "Employee added successfully"


def fetch_all_employee():
    user = mydb.forsk_coll.find()
    for i in user:
        print (i)


#Drop a collection in Mongo
mydb.forsk_coll.drop()

#Insert data in collection
add_employee(1,'Sylvester', 'Fernandes', 50000)
add_employee(2,'Yogendra', 'Singh', 70000)
add_employee(3,'Rohit', 'Mishra', 30000)
add_employee(4,'Kunal', 'Vaid', 30000)
add_employee(5,'Devendra', 'Shekhawat', 30000)

fetch_all_employee()



































