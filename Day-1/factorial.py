"""
Code Challenge
  Name: 
    Facorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""
#here we import math libreary for using their functions
import math

#now we use math liberary
#now we take input from user for find factorial

factorial_input=int(input("enter any digit for find their factorial>"))
factorial_=math.factorial

factorial_of_input=factorial_(factorial_input)

#now we print factorial of input
print ("factorial_of_input={}".format(factorial_of_input))