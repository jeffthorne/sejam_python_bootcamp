'Py Filling: Dictionaries'

'''
# A dictionary is similar to a list, but the order of items doesn’t matter, and they aren’t selected by an offset such as 0 or 1. 
# Instead, you specify a unique key to associate with each value. 
# This key is often a string, but it can actually be any of Python’s immutable types: boolean, integer, float, tuple, string, etc
# In other languages, dictionaries might be called associative arrays, hashes, or hashmaps. 
# In Python, a dictionary is also called a dict to save syllables. 
'''



empty_dict = {}       											# Creates an empty dictionary
pocs = {"colin": 2, "fernando": 6, "john": 6, "casey": 1}
pocs['casey']    												# Get item by key

del pocs['colin']												# delete an item by key

print('colin' in pocs)											# test for a key in dict

pocs['colin'] = 14
print(pocs)												