'''Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner'''
#Here we have import all libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Here we read CSV file
data = pd.read_csv("C:\\Users\\BSDU ADMIN\\Desktop\\PYTHON\\Day-14\\thanksgiving-2015-poll-data.csv", encoding="Latin-1")
#Append all csv column name into list
columns1=list(data.columns)
#create column list for rename columns names
list1=["food"+str(i) if "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply." in columns1[i] else columns1[i] for i in range(0,len(columns1))]
list1=["dish"+str(i) if "What is typically the main dish at your Thanksgiving dinner?" in list1[i] else list1[i] for i in range(0,len(columns1))]
list1=["main_dish"+str(i) if "How is the main dish typically cooked?" in list1[i] else list1[i] for i in range(0,len(columns1))]
list1=["stuffing/dressing"+str(i) if "What kind of stuffing/dressing do you typically have?" in list1[i] else list1[i] for i in range(0,len(columns1))]
list1=["cranberry saucedo"+str(i) if "What type of cranberry saucedo you typically have?" in list1[i] else list1[i] for i in range(0,len(columns1))]
list1=["pie"+str(i) if "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply." in list1[i] else list1[i] for i in range(0,len(columns1))]
list1=["desserts"+str(i) if "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply." in list1[i] else list1[i] for i in range(0,len(columns1))]
#create dictionary
dict1=dict()
#loop for for rename column names
for i in range(0,len(list1)):
    dict1[columns1[i]]=list1[i]
#rename column name
data.rename(columns = dict1, inplace = True) 
#print column names
data.columns    
#make list  
list1=list()
#for loop for fetch all food columns and append into new list
for k in data.columns:    
    if  "food" in k or "pie" in k or "desserts" in k or "dish" in k:
        list1.append(k)     
#create new list
list2=list()
#create string
string=''
#for loop for merge all food column values in one column and sep by comma
for j in range(len(data[list1[0]])):
    for i in range(len(list1)):
        #remove nan values
        if str(data[list1[i]][j]) !="nan":            
            string = string + str(data[list1[i]][j])  + ","
    #remove colmma from first index
    list2.append(string[:-1])
    string=""
#make new column by new list data
data["all food"]=list2
#Discover regional and income-based patterns in what Americans eat for Thanksgiving dinner
df_data=data.groupby(['US Region', 'How much total combined money did all members of your HOUSEHOLD earn last year?','all food']).groups
print(df_data)
        




'''Convert the column name to single word names'''
columns1=list(data.columns)
#create column list for rename columns names
list1=["food"+str(i) if "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply." in columns1[i] else columns1[i] for i in range(0,len(columns1))]
list1=["dish"+str(i) if "What is typically the main dish at your Thanksgiving dinner?" in list1[i] else list1[i] for i in range(0,len(columns1))]
list1=["main_dish"+str(i) if "How is the main dish typically cooked?" in list1[i] else list1[i] for i in range(0,len(columns1))]
list1=["stuffing/dressing"+str(i) if "What kind of stuffing/dressing do you typically have?" in list1[i] else list1[i] for i in range(0,len(columns1))]
list1=["cranberry saucedo"+str(i) if "What type of cranberry saucedo you typically have?" in list1[i] else list1[i] for i in range(0,len(columns1))]
list1=["pie"+str(i) if "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply." in list1[i] else list1[i] for i in range(0,len(columns1))]
list1=["desserts"+str(i) if "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply." in list1[i] else list1[i] for i in range(0,len(columns1))]
#create dictionary
dict1=dict()
#loop for for rename column names
for i in range(0,len(list1)):
    dict1[columns1[i]]=list1[i]
#rename column name
data.rename(columns = dict1, inplace = True) 
#print column names
data.columns






'''Using the apply method to Gender column to convert Male & Female'''
#create function for apply method to Gender column to convert Male & Female into 0 and 1
def gender_change(i):  
    if (i == "Male") :
        return 0
    elif (i == "Female") :
        return 1
#apply method and change values
data['What is your gender?']=data['What is your gender?'].apply(gender_change)
#print change male and female string into 0 and 1
data['What is your gender?']




'''Using the apply method to clean up income'''
'''(Range to a average number, X and up to X, Prefer not to answer to NaN)'''
#import librarie
import numpy as np
#replace 'Prefer not to answer' by nan value
data["How much total combined money did all members of your HOUSEHOLD earn last year?"]=data["How much total combined money did all members of your HOUSEHOLD earn last year?"].replace("Prefer not to answer",np.nan)
#crete function for clean income
def clean_income(value):
    if "to" in str(value):
        value = value.replace(",", "")
        value = value.replace("$", "")
        a,b=value.split(" to ")
        return (int(a) + int(b))/2
    elif value == "$200,000 and up":
        return 200000
#apply method and change values
data["clean_income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(clean_income)
#print clean up income
data["clean_income"]






'''compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?'''
#count values of cranberry saucedo column    
data["cranberry saucedo8"].value_counts()
#create dataframe  for homemade cranberry
homemade = data[data["cranberry saucedo8"] == "Homemade"]
#create dataframe  for canned cranberry
canned = data[data["cranberry saucedo8"] == "Canned"]
#find mean for homemade cranberry column value
a=homemade['clean_income'].mean()
#find mean for canned cranberry column value
b=canned['clean_income'].mean()
#import libraries for plot graph
import matplotlib.pyplot as plt; 
#plot bar graph for compare income between people who tend to eat homemade cranberry sauce for Thanksgiving vs people who eat canned cranberry sauce
plt.bar(['Homemade','Canned'],[a,b])
plt.show()





'''find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).'''
#group data of cranberry saucedo column
grouped = data.groupby("cranberry saucedo8")
#find average of cranberry saucedo
average_income=grouped["clean_income"].mean()
#print average cranberry saucedo
print(average_income)   


    
    

    
'''Plotting the results of aggregation'''
#find average of cranberry saucedo
average_income=grouped["clean_income"].mean()   
#average_income=grouped["clean_income"].aggregate(np.mean)
#plot bar graph for results of aggregation  
average_income.plot.bar()
plt.show()




  
'''Do people in Suburban areas eat more Tofurkey than people in Rural areas?'''
#group data of How would you describe where you live? column by dish2 column 
grouped = data.groupby("How would you describe where you live?")["dish2"]
#apply lamnda function for count grouped data values
fill_=grouped.apply(lambda x:x.value_counts())    
#change series into dictionary
my_dict=dict(fill_)
#plot bar graph between Suburban areas eat more Tofurkey than people in Rural areas?
plt.bar(['Suburban','Rural'],[my_dict[(list(my_dict.keys())[4])],my_dict[(list(my_dict.keys())[11])]])
plt.show()




'''Where do people go to Black Friday sales most often?'''
#create dataframe for people go to Black Friday sales most often
sales=data[(data["Will you shop any Black Friday sales on Thanksgiving Day?"]=='Yes')]
#count all values by region name 
sales['US Region'].value_counts()





'''Is there a correlation between praying on Thanksgiving and income?'''
#find mean by correlation between praying on Thanksgiving and income?
#mean for which people who pray 
pray_yes=data["clean_income"][data["Do you typically pray before or after the Thanksgiving meal?"]=="Yes"].mean()
#mean for which people people who pray 
pray_no=data["clean_income"][data["Do you typically pray before or after the Thanksgiving meal?"]=="No"].mean()
#plot graph between people who pray and people who pray  basis of income
plt.bar(['Pray Yes','Pray No'],[pray_yes,pray_no])
plt.show()







'''What income groups are most likely to have homemade cranberry sauce?'''
#group data by ncome groups are most likely to have homemade cranberry sauce? and change into list
homemade_cranberry=data[data["cranberry saucedo8"]=="Homemade"]['clean_income'].value_counts().tolist()
#create pie chart
plt.pie(homemade_cranberry)
plt.show()




'''Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes'''
#create dataframe for People who have Turducken and Homemade cranberry sauce seem to have high household incomes
Turducken_Homemade=data[(data['dish2']=="Turducken")&(data["cranberry saucedo8"]=="Homemade")] 
#find mean 
Turducken_Homemade=Turducken_Homemade['clean_income'].mean()
#create dataframe for People who eat Canned cranberry sauce tend to have lower incomes 
Canned=data[data["cranberry saucedo8"]=="Canned"] 
#find mean 
Canned=Canned['clean_income'].mean()
#create dataframe for who also have Roast Beef have the lowest incomes
Roast_Beef=data[data["dish2"]=="Roast beef"] 
#find mean
Roast_Beef=Roast_Beef['clean_income'].mean()
#import librarie
import matplotlib.pyplot as plt; 
labels = 'Turducken and Homemade cranberry sauce', 'Canned cranberry sauce', 'Roast Beef'
#create pie chart between means 
plt.pie([Turducken_Homemade,Canned,Roast_Beef], labels=labels, autopct='%1.2f%%', shadow=True, startangle=90)
plt.show()





'''Find the number of people who live in each area type (Rural, Suburban, etc)
who eat different kinds of main dishes for Thanksgiving:'''
#grouped data basis of How would you describe where you live? and main_dish4 column
grouped = data.groupby("How would you describe where you live?")["main_dish4"]
#create lambda function for count values of grouped data
grouped.apply(lambda x:x.value_counts())      















