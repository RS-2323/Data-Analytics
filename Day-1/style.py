"""
Code Challenge
  Name: 
    Styling of String
  Filename: 
    style.py
  Problem Statement:
    Convert to uppercase character
    Convert to lower character 
    Convert to CamelCase or TitleCase.
  Hint: 
    Try to find some function in the str class and see its help on how to use it.
    Using dir and help functions
  Input:
    Take the name as input from the keyboard. 
    ( SyLvEsTeR )
"""

user_input=input("enter input>")
print("Convert to uppercase character:{}".format(user_input.upper()))
print("Convert to lower character :{}".format(user_input.lower()))
print("Convert to CamelCase or TitleCase:{}".format(user_input.title()))