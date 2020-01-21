"""
Code Challenge 3
Write a python code to insert records to a sqlite
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.
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
c.execute("INSERT INTO students VALUES (180612017,'Riya', 'Sharma', MLAI)")
c.execute("INSERT INTO students VALUES (180612016,'Sapna', 'Saini', MLAI)")
c.execute("INSERT INTO students VALUES (180612014,'Lakshya', 'Jain', MLAI)")
c.execute("INSERT INTO students VALUES (180612012,'Lavish', 'Sharma', MLAI)")
c.execute("INSERT INTO students VALUES (180612007,'Dushyant', 'Khinchi', MLAI)")
c.execute("INSERT INTO students VALUES (180612011,'Ashwini', 'Dhankar', MLAI)")
c.execute("INSERT INTO students VALUES (180612010,'Ankit', 'Jhanjaria', MLAI)")
c.execute("INSERT INTO students VALUES (180612009,'Dinesh', 'Prajapat', MLAI)")
c.execute("INSERT INTO students VALUES (180612006,'Vishal', 'Singh', MLAI)")
c.execute("INSERT INTO students VALUES (18061205,'Shubham', 'Luxkar', MLAI)")
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