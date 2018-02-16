#                       What is a keyword argument?

'''
We've learned that positional arguments are reliant on the fact that the info
passed into the function must be in the same order.  In a keyword argument
however, it does not matter which order you pass the arguments into the
parameters.
'''


def describe_pet(animal_type, pet_name):
    # Displays information about the pet
    print ("\nI have a {0}.".format(animal_type))
    print ("My {0}'s name is {1}.".format(animal_type, pet_name))


describe_pet(animal_type="German Shepard", pet_name="California")

'''
You can see that below the code executed properly.  It does not matter which
way we introduced the arguments because we defined them while calling the
function so the computer knows where to put it regardless.

Results:
    I have a German Shepard.
    My German Shepard's name is California.
'''
