"""
Code Challenge 
import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker

"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:\\Users\\BSDU ADMIN\\Desktop\\Day-13\\Automobile.csv")
top_car=df['make'].value_counts()
df = pd.DataFrame(top_car)
print(df.head(10))

plt.pie(df["make"][0:10],labels=df.index[0:10],explode=(0.15, 0, 0, 0, 0,0,0,0,0,0),autopct='%1.1f%%')
