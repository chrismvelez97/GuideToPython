#                           What is a module alias?

'''
A module alias is similiar to a function alias but instead of importing functions and giving
them aliases, we are instead giving the modules aliases.  This does not allow us to get
away with not using dot notation, however.
'''
import modules as m

m.make_pizza(5, "pepperoni")
#   results: Making a 5-inch pizza with the following toppings
