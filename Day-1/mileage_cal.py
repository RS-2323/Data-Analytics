"""
Code Challenge
  Name: 
    Gas Mileage Calculator
  Filename: 
    mileage_cal.py
  Problem Statement:
    Assume my car travels 100 Kilometres after putting 5 litres of fuel. 
    Calculate the average of my car. 
  Hint: 
    Divide kilmeters by the litres used to get the average
"""
#assume my car travels 100 kilometers
travels=int(input("enter travel distance>"))

#after putting 5 liters of fuel
fuel=int(input("enter total fuel>"))

#now calculate average of car
average=(travels/fuel)

#now print average
print ("average of car={}".format(average))

      
