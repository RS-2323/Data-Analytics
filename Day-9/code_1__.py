
from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

url = "http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"


browser = webdriver.Chrome("c:/chromedriver.exe")



browser.get(url)

sleep(2)

 
school_code = browser.find_element_by_name("treg")
code="2000"
school_code.send_keys(code)




get_school_result = browser.find_element_by_xpath('//*[@id="ctrltr"]/td[3]/input[1]')

get_school_result.click()



 
html_page = browser.page_source

soup = BS(html_page,"lxml")

all_tables=soup.find_all('table')

print (len(all_tables))

right_table=soup.find('table', id ="Table4")

print (right_table)

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
J=[]
K=[]
L=[]
M=[]


my_table = right_table.findAll('tr')

print(my_table)
a=0
for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    #states = row.findAll('th')
    a=a+1
    if len(cells) == 13 and a>=3:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        G.append(cells[6].text.strip())
        H.append(cells[7].text.strip())
        I.append(cells[8].text.strip())
        J.append(cells[9].text.strip())
        K.append(cells[10].text.strip())
        L.append(cells[11].text.strip())





from collections import OrderedDict

col_name = ["Reg. No.","Name","I Lang-I","I Lang-II","Eng","Hindi/GK","Social Science","Phy","Chem","Bio","Maths","IT","Result"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F,G,H,I,J,K,L]))

import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("DATA.csv")


browser.quit()