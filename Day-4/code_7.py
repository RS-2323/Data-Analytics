"""
Code Challenge 2
Write a generator "trange", which generates a sequence of time tuples from 
start to stop incremented by step.
 A time tuple is a 3-tuple of integers: (hours, minutes, seconds)

Example
for time in trange((10, 10, 10), (13, 50, 15), (0, 15, 12) ):
    print(time)

will return

(10, 10, 10)
(10, 25, 22)
(10, 40, 34)
(10, 55, 46)
(11, 10, 58)
(11, 26, 10)
(11, 41, 22)
(11, 56, 34)
(12, 11, 46)
(12, 26, 58)
(12, 42, 10)
(12, 57, 22)
(13, 12, 34)
(13, 27, 46)
(13, 42, 58)
"""
'''list1=[[10, 10, 10],[13, 50, 15],[0, 15, 12]]

result = map(lambda x, y: x + y, list1[0], list1[2]) 
print(tuple(result)) '''

my_list2=list()
my_tuple2=tuple()
def count_avg(my_tuple):
    

    for i in my_tuple:
        yield i
my_tuple=((10, 10, 10),(13, 50, 15),(0, 15, 12))   
n=count_avg(my_tuple)



for i in range(0,len(my_tuple)):
    my_list2.append(next(n))
    my_tuple2=tuple(my_list2)
    
    result = map(lambda x, y: x + y, my_tuple2[0], my_tuple2[2])
    print(tuple(result))
    
    
list1=[10, 10, 10]
list2=[13, 50, 15]
list3=[0, 15, 12]

if(list1[0]==list2[0] or list1[0]==list2[0] or list1[0]==list2[0]):
    print("TRUE")
else:
    print("FALSE")
my_accdic_list=['twitter','overthinking','timepass']
list_of_addic=['facebook','instagram','twitter','whatsapp','snapchat']
for fav_addic in list_of_addic:
    if(fav_addic in my_accdic_list):
        print(fav_addic)
        


