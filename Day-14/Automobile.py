"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""
import pandas as pd
df = pd.read_csv("C:\\Users\\BSDU ADMIN\\Desktop\\Day-14\\Automobile.csv")
#1. Handle the missing values for Price column
df[df['price'].isnull()]
df2 = df.fillna(0)
print(df2['price'])
print(df2)

#2. Get the values from Price column into a numpy.ndarray
import numpy as np

array1=np.array(df2['price'])
print(array1)

#3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price

np.min(df['price'])
np.max(df['price'])
np.mean(df['price'])
np.std(df2['price'])