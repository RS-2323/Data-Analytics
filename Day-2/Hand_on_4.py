# Hands On 4  
"""
cats_and_dogs = ["cat", "cat", "dog", "cat", "dog", "dog"]
We all know that cats and dogs don't get along. 
Iterate over the array and delete the elements that represent dogs.
"""
cats_and_dogs = ["cat", "cat", "dog", "cat", "dog", "dog"]
k=list()
for i in cats_and_dogs:
    if(i!="dog"):
        print (i)
        k.append(i)
print(k)
