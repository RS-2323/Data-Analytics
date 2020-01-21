"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is 
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""

user_input=input("enter number series>").split(",")



user_input = [int(i) for i in user_input]


user_input_=sorted(user_input)
#print (user_input_)
#print (min(user_input_))
#print (max(user_input_))

user_input_.pop(0)
user_input_.pop()
#print (user_input_)
average=(sum(user_input_)/len(user_input_))
print(float(average))




