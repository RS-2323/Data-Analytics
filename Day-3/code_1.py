
#Find all of the numbers from 1-1000 that are divisible by 7

k=[i for i in range(1,1000) if (i%7==0)]
print(k)
print("\ntotal number ={}".format(len(k)))


