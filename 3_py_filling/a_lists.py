'Py Filling: [Lists], Tuples, Dictionaries, and, sets'
'''
You’ve already seen Python strings, which are sequences of characters. 

Python has two other sequence structures: tuples and lists. These contain zero or more elements. 
Unlike strings, the elements can be of different types.

Why does Python contain both lists and tuples? 
Tuples are immutable; when you assign elements to a tuple, they’re baked in the cake and can’t be changed. 

Lists are mutable, meaning you can insert and delete elements with great enthusiasm. 
'''


[]
list()

ne_sales_engineers = ['mondeux', 'colin', ' fernando', ' john', ' kaz', ' Anthony']
sales_reps = list()

[x for x in ne_sales_engineers if x != 'colin']					# what happens to colin?
ne_sales_engineers.insert(len(ne_sales_engineers), 'colin')



print(list('deep security'))									# string to list

poc_end_date = '1/9/2017'
print(poc_end_date.split('/'))

ne_sales_engineers[0:2]  										# Can also slice a list -> ['mondeux', ' colin']


# Combine lists by using extend() or +=
east_sales_engineers = ['westphal', 'chris', 'kenJo', 'Vitaliy', 'Geoff']
ne_sales_engineers.extend(east_sales_engineers)
print(ne_sales_engineers)

# or 
ne_sales_engineers += east_sales_engineers
