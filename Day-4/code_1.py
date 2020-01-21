"""
Code Challenge

Consider the following problem, where you want to create a new dictionary 
where the key is a number divisible by 2 in a range of 0-10 and 
it's value is the square of the number. 

First write the solution using for loop and then rewrite using Comprehension
"""
num_dict=dict()
#First write the solution using for loop
for num in range(0,10):
    if (num%2==0):
        num_dict[word] = num**2    

print(num_dict)



#rewrite using Comprehension
new_dict = {key: key ** 2 for key in range(0,10) if key%2==0}
print(new_dict)
    