"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""
user_input=input("enter string>")

Character_Frequency={}
for i in user_input:
    if i in Character_Frequency:
        
        Character_Frequency[i] +=1
    else:
        Character_Frequency[i] =1
print (str(Character_Frequency))
        
        
    