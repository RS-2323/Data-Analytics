"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
list1=list()
user_input=input("enter number list>").split(" ")
k=[i for i in user_input]

for i in k: 
    if(i==i[::-1] or i[0]=="-"):
        if(i[0]=="-"):
            list1.append(False)
        else:
            list1.append(True)
    
print (all(list1)) 





















