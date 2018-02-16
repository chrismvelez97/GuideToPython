#                               What is inheritance?
import classes_part1 as c

'''
Sometimes, we might have class that is great but only in general.  As
you can tell, there are many types of dogs and so we can create
even more specific classes for specific types of dogs.

However, rather than reinventing the wheel and creating the same class
blueprint over again, with some additional methods and attributes, we
can have our newer specific class inherit from the dog class.

The dog class will remain the parent class and the new class will
inherit from it as the child of the dog class.

Everything the dog class the child class will have as well with some
additional attributes, as well as methods.

Here, we imported classes_part1 as c because I'm lazy and don't want to
keep typing classes_part1 everytime I access that module
'''


class GermanShepard(c.Dog):
    '''
    Above, you'll see we included the Dog class but with dot notation
    This is only because we imported our class from a module
    Normally, you'd just be able to refer to your class as it's name
    but only if it's within the same file and given that the parent
    class is at the top of the file.
    '''

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    #   Here we overrode the original display function so it would work with our new
    #   attribute.
    def displayInfo(self):
        print ("\nName: {0}\nAge: {1}\nColor: {2}".format(
            self.name.title(), int(self.age), self.color.title()))


my_dog = GermanShepard(name="california", age=10, color="golden brown")
my_dog.displayInfo()
'''
Results:
Name: California
Age: 10
Color: Golden Brown
'''
