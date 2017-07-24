'Py Ingredients: Variables, Numbers, [Strings]'

'''
* Because of its support for the Unicode standard, Python 3 can contain characters from any written language in the world, plus a lot of symbols. 
* You make a Python string by enclosing characters in either single quotes or double quotes.
'''

'Sales Engineer'    #single quotes
"Sales Rep"         #double quotes
"Look at Fernando's salesy slide deck!"   #single quotes embedded in double

#triple quotes can multiple lines. Used as documentation as well.
ds_elevator_pitch = """
					Server security for physical, virtual, and cloud deployments should perform in a way 
					that fits each environment efficiently and consistently. Trend Micro protects your 
					servers without slowing you down.
					"""

# You can do cool stuff with Strings
print(ds_elevator_pitch.find('you'))     		#175
print(str(98.6))								# type conversion
print('abc' + 'def')							#string concatenation
print(ds_elevator_pitch[8]) 					#r

'''
Slice with [start : end : step ] -> allows you to extract a substring(a part of a string from a string by using a slice)
'''

ds_elevator_pitch[:]							# is the same as 0:  (the entire string)
ds_elevator_pitch[20:]      					# from offset 20 to the end
ds_elevator_pitch[-3:]      					# the last 3 characters


len(ds_elevator_pitch)  						#gets the length of a string in characters


sales_engineers = 'mondeux, colin, fernando, john, kaz, Anthony'
print(sales_engineers.split(',')).   		# rsplit a string with split -> eturns a list ['mondeux', ' colin', ' fernando', ' john', ' kaz', ' Anthony']

