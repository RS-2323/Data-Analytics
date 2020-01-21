"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
  Hint:
      Try to use enumerate
"""
k=list()
user_input=input("enter number>").split(",")
user_input1=(list(enumerate(user_input)))


for index,ele in enumerate(user_input):
    if ele =="13" and index<len(user_input)-1 and user_input[index+1]!="13":
        #print(user_input[index+2])
        k.append(user_input[index+2])
#print(k)
k=[int(i) for i in k]
print(sum(k))

    

