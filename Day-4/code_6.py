"""
Code Challenge 1
Write a generator which computes the running average from the list
[7, 13, 17, 231, 12, 8, 3]
"""
my_list2=list()
def count_avg(my_list):
    

    for i in my_list:
        yield i
my_list=[7, 13, 17, 231, 12, 8, 3]   
n=count_avg(my_list)


for i in range(0,len(my_list)):
    my_list2.append(next(n))
    print(sum(my_list2)/len(my_list2))
    
   





