"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse2.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a integer.
    Take input from User  
  Input: 
    -321
  Output:
    -123  
"""
user_input=input("enter dight>")
if(user_input[0]=="-"):
    char = user_input[0]
    user_input = user_input.replace(char, '')
print(char + user_input[::-1])
