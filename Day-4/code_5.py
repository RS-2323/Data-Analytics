"""
Code Challenge 7

https://github.com/thecbp/blog_data/blob/master/recipeData.csv

The data contains important beer characteristics from brewers around the world, 
including style of beer, alcohol by volume (ABV), and amount of beer produced.

"""

def csv_read(data):
    for row in data:
        yield row
data = open('C:\\Users\\Om\\Desktop\\PYTHON\\Day_4\\recipeData.csv',"rt")
n = csv_read(data)
next(n)

    
       

