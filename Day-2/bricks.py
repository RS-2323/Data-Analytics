"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""
user_input=input("enter number>").split(",")

list1=[int(i) for i in user_input]
j=list1[0]*1
p=list1[1]*5
s=j+p
if(s>=list1[2]):
    
    print(True)
else:
    print(False)

'''list1=[1,2,11]
print(list1[:2])'''
