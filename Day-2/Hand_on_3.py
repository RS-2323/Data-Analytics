# Hands On 3  
"""
odds_and_evens = [1, 3, 2, 18, 5, 10, 24]
iterate over the array and return any even numbers. 
iterate over the array and return only the first array element that is odd

"""
k=list()   
odds_and_evens = [1, 3, 2, 18, 5, 10, 24]
#iterate over the array and return any even numbers. 
odds_and_evens1 = enumerate(odds_and_evens) 
odds_and_evens2=list(odds_and_evens1)

for items,eve in odds_and_evens2:
    #print(items,eve)
    if(eve%2==0):
        #print(eve)
        k.append(eve)
print(k[0])
''' 
for items,eve in odds_and_evens2:
    #print(items,eve)
    if(eve%2!=0):
        #print(eve)
        k.append(eve)
print(k[0])'''


odds_and_evens = [1, 3, 2, 18, 5, 10, 24]
for i in list(enumerate(odds_and_evens)):
    if(i[1]%2==0):
        print(i[1])