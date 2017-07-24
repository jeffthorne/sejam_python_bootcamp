'Py Filling: Tuples'

'''
* Similar to lists, tuples are sequences of arbitrary items. 
* Unlike lists, tuples are immut‐ able, meaning you can’t add, delete, or change items after the tuple is defined. 
* So, a tuple is similar to a constant list.
'''

empty_tuple = ()


one_se = 'Tim',   # To make a tuple with one or more elements, follow each element with a comma.

se_tuple = 'Tim', 'Hai', 'Fontaine'

print(len(se_tuple))

east_se_tuple = tuple(['westphal', 'chris', 'kenJo', 'Vitaliy', 'Geoff'])          #list to tuple
print(east_se_tuple)


'''
You can often use tuples in place of lists, but they have many fewer functions—there is no append(), insert(), 
and so on—because they can’t be modified after creation

Why not just use lists then?
	* Tuples use less space
	* You can’t clobber tuple items by mistake
	* You can use tuples as dictionary keys,
	* etc
'''