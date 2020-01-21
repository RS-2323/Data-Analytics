#Remove all of the vowels in a string
string="ria sharma"
char_vol=['A','E','I','O','U','a','e','i','o','u']
char1=[string.replace(char,"") for char in char_vol if(char in string)]
print(char1[0])
