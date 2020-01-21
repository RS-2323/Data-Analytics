"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""
user_input=input("enter string>")
count=0
count1=0
for i in user_input:
    if(i.isdigit()):
       
        count=count+1
    if(i.isalpha()):
        count1=count1+1
print("total digit in {} ={}".format(user_input,count))
print("total char in {} ={}".format(user_input,count1))
