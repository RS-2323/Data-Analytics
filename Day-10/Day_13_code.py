
#1. Which Male and Female Professor has the highest and the lowest salaries
import pandas as pd
df = pd.read_csv("C:\\Users\\BSDU ADMIN\\Desktop\\Day-13\\Salaries.csv")
df.groupby('sex')[['salary']].max()
df.groupby('sex')[['salary']].min()



#2. Which Professor takes the highest and lowest salaries.
df_sub= df[(df['rank'] =='Prof')]
print(df_sub.max()) 
print(df_sub.min())

#3. Missing Salaries - should be mean of the matching salaries of those 
#   whose service is the same
Missing_Salaries=df['salary'].fillna(round(df['salary'].mean()))
print(Missing_Salaries)
df_sub=df[df['salary'].isnull()]
print(df_sub)


#4. Missing phd - should be mean of the matching service 
Missing_phd=df['phd'].fillna(round(df['phd'].mean()))
print(Missing_phd)



#5. How many are Male Staff and how many are Female Staff. 
df['sex'].value_counts()



#   Show both in numbers and Graphically using Pie Chart. 
import matplotlib.pyplot as plt 
labels=['male','female']
list1= df['sex'].value_counts(normalize = True).tolist()
plt.pie(list1,labels=labels,autopct='%1.1f%%')



#   Show both numbers and in percentage
df['sex'].value_counts(normalize = True)

#6. How many are Prof, AssocProf and AsstProf. 
df['rank']
df['rank'].value_counts()


#   Show both in numbers adn Graphically using a Pie Chart
import matplotlib.pyplot as plt 
labels=['Prof','AsstProf','AssocProf']
list2= df['rank'].value_counts(normalize = True).tolist()
plt.pie(list2,labels=labels,autopct='%1.1f%%')

#7. Who are the senior and junior most employees in the organization.
df_sub= df[(df['service'] ==df['service'].min())]
print(df_sub)
df_sub1= df[(df['service'] ==df['service'].max())]
print(df_sub1)



#8. Draw a histogram of the salaries divided into bin starting 
#  from 50K and increment of 15K
import matplotlib.pyplot as plt
x = df['salary']
plt.hist(x, bins=range(50000,200000,15000))
plt.xlabel("Salaries")
plt.show()




