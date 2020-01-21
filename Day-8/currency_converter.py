"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""

import requests
import time
curr1=input("enter>")
curr2=input("enter>")
curr3=curr1+"_"+curr2
url2 = "?q={}".format(curr3)
url1 = "https://free.currconv.com/api/v7/convert"
url2 = "?q={}".format(curr3)
url3 = "&compact=ultra&apiKey=1dea270000e79bc5f889"
'1dea270000e79bc5f889'
url = url1 + url2+url3
response=requests.get(url)
jsondata=response.json()
print(jsondata[curr3])


