
# Hands On 7 
# Make a function to find whether a year is a leap year or no, return True or False 
user_year = int(input("Enter the Year>"))

if (user_year%400 == 0):
    print("Leap Year")
elif (user_year%4 == 0):
    print("Leap Year")
elif (user_year%100 == 0):
    print("%s is Not the Leap Year")
else:
    print("Not a the Leap Year")
