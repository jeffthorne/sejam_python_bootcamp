'Py Crust: Functions'
# way of organizing larger code into manageable pieces 


def say_hello():
	print("Hello")

say_hello()


def say_hello(name):
	print("Hello", name)


say_hello("Alice")


# Positional Arguments
def menu(wine, entree, dessert):
	return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken', 'cake'))
print(menu('beef', 'bagel', 'bordeaux'))



#Keyword Arguments 
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
print(menu('frontenac', dessert='flan', entree='fish'))					#you can mix keyword arguments. positional needs to come first.




#default parameter values
def menu(wine, entree, dessert='pudding'):
	return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chardonnay', 'chicken')
menu('dunkelfelder', 'duck', 'doughnut')



# Gather Positional Arguments with *  -> gathers positional arguments into a tuple
def print_args(*args):
	print('Positional argument tuple:', args)


print_args(3, 2, 1, 'wait!', 'uh...')



# Gather Keyword Arguments with ** ->> gathers keyword arguments into dict
def print_kwargs(**kwargs):
	print('Keyword arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


