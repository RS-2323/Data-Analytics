# Hands On 6
"""
quiet_and_loud = ["hi", "HI", "shhh", "WHAT?!"]
terate over the array to determine if any of the words contained there are loud (upcased).
"""
quiet_and_loud = ["hi", "HI", "shhh", "WHAT?!"]

for i in quiet_and_loud:
    if(i[0].isupper()):
        print(i)
        
