'Py Filling: Sets'

'''
# A set is like a dictionary with its values thrown away, leaving only the keys. 
# As with a dictionary, each key must be unique. 
# You use a set when you only want to know that something exists, and nothing else about it. 
# Use a dictionary if you want to attach some information to the key as a value. 
'''

empty_set = ()
even_numbers = {0,2,4,6,8}
print(8 in even_numbers)

east_sales_engineers = set(['westphal', 'chris', 'kenJo', 'Vitaliy', 'Geoff'])
print(east_sales_engineers)
print(type(east_sales_engineers))