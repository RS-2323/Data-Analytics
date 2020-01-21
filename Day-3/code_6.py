#A list of all consonants in the sentence 'The quick brown fox jumped over the lazy dog'
string=("The quick brown fox jumped over the lazy dog")
conso=['Q','W','R','T','Y','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
con=[i for i in string if(i in conso)]
print(list(con))

