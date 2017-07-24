'Py Objects and Classes'

# An object contains both data (variables, called attributes) and code (functions, called methods)
# __init__() is a special Python name for a method that initializes an individual object from its class definition.  
# Python uses the self argument to find the right object’s attributes and methods. 



class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return self.first_name + " " + self.last_name

    def what_am_i(self):
        return "I am %s of type %s" % (self.full_name(), type(self))


alice = Person("Alice", "Martin", 30)
joe = Person("Joe", "Smith", 32)
print(alice.first_name)
print(alice.age)
print(alice.__dict__)


'Inheritance'
# creating a new class from an existing class but with some additions or changes. 
# It’s an excellent way to reuse code. 

class Employee(Person):

    def __init__(self, first_name, last_name, age, employee_id):
        super().__init__(first_name, last_name, age)
        self.employee_id = employee_id


    def what_am_i(self):
        return "I am %s of type %s" % (self.full_name(), type(self))



bob = Employee("Bob", "Smith", 27, 123456)


'Polymorphism'
# the ability to present the same object interface for differing underlying forms (types)

people = [alice, bob]
for person in people:
    print(person.what_am_i())




