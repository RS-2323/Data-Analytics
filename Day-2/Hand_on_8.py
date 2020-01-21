# Hands On 8
# Make a function days_in_month to return the number of days in a specific month of a year

def days_in_month(user_month):
    if(user_month=="January" or user_month=="March" or user_month=="July" or user_month=="September" or user_month=="November" or user_month=="January"):
        return '31 days in {}'.format (user_month) 
    if(user_month=="April" or user_month=="June" or user_month=="August" or user_month=="October" or user_month=="November" or user_month=="December"):
        return '30 days in {}'.format (user_month)
    elif(user_month=="February"):
        return '28 days in {}'.format (user_month)

    else:
        return None
user_month=input("enter month>")
print(days_in_month(user_month))

