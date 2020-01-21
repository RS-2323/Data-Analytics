"""
Code Challenge
  Name: 
    Ride Cost Calculator
  Filename: 
    ridecost_cal.py
  Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office. 
  Hint: 
"""  

#take input from user for thier tarvel distance
travel=int(input("enter your per day travel>"))

#take input from user for thier cost of dieasel per liter
cost=int(input("enter cost of dieasel>"))

#take input from user therir car average

average=int(input("enter average of car>"))

#Now calculate the cost of driving per day to office

cost_of_driving=(round(travel/average)*cost)

#now print calculate the cost of driving per day to office
print ("cost of driving per day={}".format(cost_of_driving))
 
 

