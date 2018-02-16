#                     Default values and Modifying attributes


class Character():
    """
    This class will model a character in a videogame
    to show the different things we can do with classes.
    """

    def __init__(self, name):
        '''
        You can see we have attributes we didn't require
        in our parameters but the reason for this is
        because we are setting default values.
        '''
        self.health = 100
        self.strength = 20
        self.name = name

    def displayInfo(self):
        print ("Congratulations!")
        print ("\nYou have created a brand new character")
        print ("This is you!\nName: {0}\nHealth: {1}\nStrength: {2}".format(
            self.name, str(self.health), str(self.strength)
        ))

    def fall(self):
        '''
        You can see below that we changed the default value
        to drop in case our character's health fell.

        You can also change attributes values directly through
        your instance(See line 65 for example)
        '''
        self.health -= 10
        print ("\nUh oh! Seems like you're pretty clumsy! \n\n You get back up but lose ten health")


ryu = Character(name="Ryu")
ryu.displayInfo()
'''
Results:
Congratulations!

You have created a brand new character
This is you!
Name: Ryu
Health: 100
Strength: 20
'''

ryu.fall()
'''
Results:
Uh oh! Seems like you're pretty clumsy!

 You get back up but lose ten health
'''

print (ryu.health)

#   This is kinda cheating because we wouldn't want our user
#   To be able to just reset their health but I'm just
#   showing this as an example.
ryu.health = 100

ryu.displayInfo()
'''
Results:
You have created a brand new character
This is you!
Name: Ryu
Health: 100
Strength: 20
'''
