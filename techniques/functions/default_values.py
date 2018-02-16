#                        What are default values?

'''
Default values are values that you can set automatically so the parameter
values are already filled, and are changed in case the case changes.
I'm not going to lie that's a pretty bad explanation but if you look at the
following code it might make more sense.

It should be noted that any default values being set, must be the last
parameters so that positional arguments will still work.
'''


def describe_pet(pet_name, animal_type="dog"):
    print ("\nI have a {0}.".format(animal_type))
    print ("My {0}'s name is {1}.".format(animal_type, pet_name))


#   Ex.1
describe_pet(pet_name="California")

'''
Notice how in our function, we set the default value of animal type to dog, so
when we call the functin we can just pass the pet's name

Results:
    I have a dog.
    My dog's name is California.
'''

#   Ex.2
describe_pet(animal_type="cat", pet_name="alex")

'''
Notice here how even though our function defines the animal type with a default
value, we changed it to something else, and used keyword arguments to enter the
information.

Results:
    I have a cat.
    My cat's name is alex.
'''
