"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""
user_input = input("Enter a character: ")
for v in 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM':
   user_input=user_input.replace(v,v+'o'+v)
print(user_input)


