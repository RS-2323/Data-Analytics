#A list of all the capital letters (and not white space) in 'The Quick Brown Fox Jumped Over The Lazy Dog'
string="The Quick Brown Fox Jumped Over The Lazy Dog"
cap=[i for i in[j for j in string] if i.isupper()]
print(list(cap))