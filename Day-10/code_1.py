"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area
Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""
from bs4 import BeautifulSoup
import requests
wiki = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source = requests.get(wiki).text
#print(source)
soup = BeautifulSoup(source,"lxml")
all_tables=soup.find_all('table')
#print (all_tables)
#len(all_tables)
right_table=soup.find('table', class_='wikitable')
#print (right_table)
A=[]
B=[]

my_table = right_table.findAll('tr')

#print(my_table)

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 7:
        A.append(cells[1].text.strip())
        B.append(cells[4].text.strip())
from collections import OrderedDict

col_name = ["State/Territory","National share (%)"]
col_data = OrderedDict(zip(col_name,[A,B]))
# If you want to store the data in a csv file
import pandas as pd
df = pd.DataFrame(col_data)
#print (df.head(6))
import pandas as pd
import matplotlib.pyplot as plt
plt.pie(df["National share (%)"][0:5],labels=df["State/Territory"][0:5],explode=(0.15, 0, 0, 0, 0),autopct='%1.1f%%')
"""