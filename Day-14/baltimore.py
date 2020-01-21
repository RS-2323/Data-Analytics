"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    0. remove the dollar signs in the AnnualSalary field and assign it as a float
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles and Graph it
    0. Graph and show which Job Title spends the most
    0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 
    
  Hint:

import pandas as pd
import requests
import StringIO as StringIO
import numpy as np
        
url = "https://data.baltimorecity.gov/api/views/2j28-xzd7/rows.csv?accessType=DOWNLOAD"
r = requests.get(url)
data = StringIO.StringIO(r.content)

dataframe = pd.read_csv(data,header=0)

dataframe['AnnualSalary'] = dataframe['AnnualSalary'].str.lstrip('$')
dataframe['AnnualSalary'] = dataframe['AnnualSalary'].astype(float)

# group the data
grouped = dataframe.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])

# sort the data
pd.set_option('display.max_rows', 10000000)
output = aggregated.sort(['amax'],ascending=0)
output.head(15)


aggregated = grouped.agg([np.sum])
output = aggregated.sort(['sum'],ascending=0)
output = output.head(15)
output.rename(columns={'sum': 'Salary'}, inplace=True)


from matplotlib.ticker import FormatStrFormatter

myplot = output.plot(kind='bar',title='Baltimore Total Annual Salary by Job Title - 2014')
myplot.set_ylabel('$')
myplot.yaxis.set_major_formatter(FormatStrFormatter('%d'))


"""
#0. remove the dollar signs in the AnnualSalary field and assign it as a float
import pandas as pd
df = pd.read_csv("C:\\Users\\BSDU ADMIN\\Desktop\\Day-14\\Baltimore_City_Employee_Salaries_FY2014.csv")
df['AnnualSalary'] = df['AnnualSalary'].astype(float)
#0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
#       Sort the data and display to show who get the highest salary
import numpy as np
group = df.groupby(['JobTitle'])['AnnualSalary']
aggregated = group.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])
print(aggregated)


#0. Try to group on JobTitle only and sort the data and display
import numpy as np
group = df.groupby(['JobTitle'])
print(group.head(15))

#0. How many employess are there for each JobRoles and Graph it
df1=df['JobTitle'].value_counts()
df2 = pd.DataFrame(df1)
import matplotlib.pyplot as plt; 
plt.bar(range (0,5), df2['JobTitle'].head(), align='center', alpha=1.0)
plt.xticks(range (0,5), tuple(df2.index)[0:5],rotation=90)
plt.show()
#0. Graph and show which Job Title spends the most
df1=df['JobTitle'].value_counts()
df2 = pd.DataFrame(df1)
import matplotlib.pyplot as plt; 
plt.bar(range (0,5), df2['JobTitle'].head(), align='center', alpha=1.0)
plt.xticks(range (0,5), tuple(df2.index)[0:5],rotation=90)
plt.show()
#0. List All the Agency ID and Agency Name 
df[['AgencyID','Agency']]

#0. Find all the missing Gross data in the dataset 
df[df['GrossPay'].isnull()]


















