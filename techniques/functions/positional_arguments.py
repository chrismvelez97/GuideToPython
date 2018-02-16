#                       What are positional arguments?

'''
Positional arguments are arguments that must be entered in the correct order.
Putting the information in the wrong order makes the code execute incorrectly.

The cool thing about programming is that you're always learning new things.
You're never so experienced that you know everything about programming.

As I'm creating this guide I didn't even know what these were, but I
included them because they are definitly important to know to be an efficient
programmer.
'''


def describe_pet(animal_type, pet_name):
    # Displays information about the pet
    print ("\nI have a {0}.".format(animal_type))
    print ("My {0}'s name is {1}.".format(animal_type, pet_name))


describe_pet("German Shepard", "California")

'''
You can see how below including the arguments in the wrong order might execute
the code in the wrong way.

If it ran incorrectly it would say:
    I have a California
    My California's name is German Shepard

Results:
    I have a German Shepard.
    My German Shepard's name is German Shepard.
'''
