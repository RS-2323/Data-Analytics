from bs4 import BeautifulSoup
import requests

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source = requests.get(wiki).text
#or

soup = BeautifulSoup(source,"lxml")


all_tables=soup.find_all('table')

print (all_tables)

right_table=soup.find('table', class_='wikitable')

print (right_table)

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

my_table = right_table.findAll('tr')

print(my_table)

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())



from collections import OrderedDict

col_name = ["State or UN","Admin Cap","Legis Cap","Judi Cap","Year","Capital"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))

import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")



