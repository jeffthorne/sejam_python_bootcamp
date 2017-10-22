def menu(wine, entree, dessert):
	return {'wine': wine, 'entree': entree, 'dessert': dessert}


#Keyword Arguments 
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
print(menu('frontenac', dessert='flan', entree='fish'))	


meals = menu('frontenac', dessert='flan', entree='fish')

print(meals['wine'])