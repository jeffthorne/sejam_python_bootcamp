'Py Crust: Control Structures'

'if, elif, else'
# The if and else lines are Python statements that check whether a condition is True
# Testing with if, elif, and else runs from top to bottom

ne_pocs = 114

if ne_pocs < 100:
	print('wtf')
elif ne_pocs <= 114:
	print("not bad")
else:
	print('good job')


'Repeat with while'
# The simplest looping mechanism in Python is while

count = 1
while count <= 5:
	print(count)
	count += 1


#cancel with break
count = 1
while count <= 5:
	if count == 3:
		break
	print(count)
	count += 1


#skip ahead with continue
count = 1
while count <= 5:
	if count == 3:
		count += 1
		continue
	print(count)
	count += 1




'Iterate with for'
# Lists are one of Python's iterable objects. Tuple of list iteration produces an items at a time.
east_sales_engineers = ['westphal', 'chris', 'kenJo', 'Vitaliy', 'Geoff']
for se in east_sales_engineers:
	print(se)

