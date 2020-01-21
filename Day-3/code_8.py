#A list of all square numbers formed by squaring the numbers from 1 to 1000.
'''
k=list()
for i in range(1,1000):
    
    if(i**2 in range(1,1000)):
        k.append(i**2)
print([int(i) for i in k])
'''
print([i**2 for i in range(1,1000) if i**2<=1000])