"""

Code Challenge
  Name: 
    Fizz Buzz
  Filename: 
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 100(included). 
    For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz". 
  User Input 
    Not required  
  Output:
    1
    2
    Fizz
    4 
    Buzz  
"""


# decide specific range for find fuzbuzz

range_number=range(17)

for i in range_number:
    #print i
    if((i%3==0) and (i%5==0)):
        print("FizzBuzz")
    elif(i%5==0):
        print("buzz")
    elif(i%3==0):
        print("Fizz")
    else:
        print(i)
        

