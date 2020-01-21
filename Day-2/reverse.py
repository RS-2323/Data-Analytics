def reverse_func(user_input):
    user_input=user_input[::-1]
    """ My Greeting function """
    return 'reverse string is: {}'.format ( user_input) 


#Calling the function 
user_input=input("enter string>")

print(reverse_func(user_input))
