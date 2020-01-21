"""
Code Challenge

For all the numbers 1-1000, use a nested list/dictionary comprehension to find 
the highest single digit any of the numbers is divisible by 3

"""

# [result_if_condition_met if condition else result_if_condition_not_met for element in group_of_elements]
num=[val for val in range(1,1000) if (len(str(val))==1 and val %3==0)]
print(max(num))


        
    



