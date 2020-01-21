"""
Code Challenge
Use a dictionary comprehension to count the length of each word in a sentence.
"""
string="google.com"

wordCounts = { word: string.count(word) for word in string }
print(wordCounts)