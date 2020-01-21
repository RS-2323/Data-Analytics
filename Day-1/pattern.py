"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""
user_input=input("number>")
user_input=int(user_input)
for i in range(0,user_input):
    print("*"*i)
for j in range(user_input,0,-1):
    print("*"*j)
    
