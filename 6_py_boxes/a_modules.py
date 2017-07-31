'Py Boxes: Modules'

'''
A module is just a file of Python code.

Use modules when you have small functions and programs that span across some files.
'''


# module is the name of another Python file, without the .py extension
from models.person import Person    				


alice = Person("Alice", "Martin", 30)
print(type(alice))
joe = Person("Joe", "Smith", 32)
print(alice.first_name)
print(alice.age)
print(alice.__dict__)



from models.person import Person as SalesEngineer		# Import a Module by Another Name

alice = SalesEngineer("Alice", "Martin", 30)
joe = SalesEngineer("Joe", "Smith", 32)
print(alice.first_name)
print(alice.age)
print(alice.__dict__)



# Import Only What You Want from a Module
from models.person import random_function
random_function()


# Module Search Path: Where does python search for modules by default 
import sys

for place in sys.path:
	print(place)


