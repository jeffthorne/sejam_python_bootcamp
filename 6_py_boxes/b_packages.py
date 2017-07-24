'Py Boxes: Packages'

'''
A package is another way to organize your code. 

Packages let you import directories on your computer into your programs using the 'import' or 'from import' statements. 

A directory on your system can become a package if it contains an empty __init__.py

Use these when you want to have separate features in your app/software
'''

from app.models.person import Person

alice = Person("Alice", "Martin", 30)
print(alice.first_name)



