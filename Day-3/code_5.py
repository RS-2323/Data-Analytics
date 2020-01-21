#Find all of the words in a string that are less than 4 letters
string=("ria sharma is student of BSDU").split(" ")
print([a for a in[x for x in string] if(len(a)<4) ])

