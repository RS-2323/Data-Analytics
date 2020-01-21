"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""
from functools import reduce
user_input=input("enter list>").split(",")
user_input=[int(i) for i in user_input]
Add=sum(user_input)
Multiply=reduce(lambda x, y: x*y, user_input)
Largest=max(user_input)
Smallest=min(user_input)
Sorting=sorted(user_input)
Remove_Duplicates=list(dict.fromkeys(user_input))


print("Sum = {}\nMultiply = {}\nLargest = {}\nSmallest = {}\nSorted = {}\nWithout Duplicates = {}".format(Add,Multiply,Largest,Smallest,Sorting,Remove_Duplicates))
    





















