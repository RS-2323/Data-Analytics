"""
Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T
"""

user_input=input("enter string>")
char = user_input[0]
user_input = user_input.replace(char, '$')
user_input = char + user_input[1:]
print(user_input)