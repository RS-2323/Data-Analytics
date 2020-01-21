# Hands On 1  
"""
lunch_menu = ["pizza", "sandwich", "sushi", "soup", "salad"]      
Since you're super hungry and super excited about lunch,
enumerate over the array and append an "!" ("exclamation mark") 
to each menu item. 
"""

lunch_menu = ["pizza", "sandwich", "sushi", "soup", "salad"]   
print(['!{0}'.format(i) for i in lunch_menu])
  
'''
for ele in enumerate(lunch_menu):
    print (ele)  
    #print (type(ele))
lunch_menu1=enumerate(lunch_menu) 
'''
#print (list(enumerate(lunch_menu))) 
