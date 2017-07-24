
class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return self.first_name + " " + self.last_name

    def what_am_i(self):
        return "I am %s of type %s" % (self.full_name(), type(self))





def random_function():
	print("I am a random function.")