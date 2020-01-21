"""
Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""
import re
user_input=input("enter digit>")
result = re.search(r'[-+]?[0-9]*\.[0-9]*',user_input)
if(result.start()==0):
    print(True)
else:
    print(False)

