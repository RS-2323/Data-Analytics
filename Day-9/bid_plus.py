"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          
          # Optional - Do not do this
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS
browser = webdriver.Chrome("c:/chromedriver.exe")
url = "https://bidplus.gem.gov.in/bidlists"
browser.get(url)

'''
BID_NO=browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[1]/p[1]/a').text
print(BID_NO)

items=browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[2]/p[1]/span').text
print(items)

Quantity_Required=browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[2]/p[2]/span').text
print(Quantity_Required)

Department=browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[3]/p[2]').text
print(Department)

Start_Date=browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[4]/p[1]/span').text
print(Start_Date)

End_Date=browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[4]/p[2]/span').text
print(End_Date)
'''


BID_NO=[]
items=[]
Quantity_Required=[]
Department=[]
Start_Date=[]
End_Date=[]

x=10



for i in range(1,11) :
    A=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text
    B=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text
    C=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text
    D=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text
    E=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text
    F=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text
    
    


    BID_NO.append(A)
    items.append(B)
    Quantity_Required.append(C)
    Department.append(D)
    Start_Date.append(E)
    End_Date.append(F)
    x=x+1



from collections import OrderedDict

col_name = ["BID NO","items","Quantity Required","Department Name And Address","Start Date","End Date"]
col_data = OrderedDict(zip(col_name,[BID_NO,items,Quantity_Required,Department,Start_Date,End_Date]))

import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("bid_plus.csv")

browser.quit()

