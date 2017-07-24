'Py Crust: comprehensions'


'''
# A comprehension is a compact way of creating a Python data structure from one or more iterators. 
# Comprehensions make it possible for you to combine loops and conditional tests with a less verbose syntax. 
'''

#. [ expression for item in iterable ]

number_list = [1,2,3,4,5,6]
number_list = list(range(1,7))


add_one_list = [x + 1 for x in number_list]
print(add_one_list)

even_number_list = [x for x in number_list if x % 2 == 0]
print(even_number_list)