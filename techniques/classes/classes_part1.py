#                                   What are classes?

'''
So, the further we get into Object-Oriented programming the further we get into to using,
objects to solve problems.  One of those tools we have for automatically creating objects,
are classes.

Classes are blocks of code that instantly create objects with default
functions and variables.  When a function is part of a class, we refer to it as a method,
and when we have a variable in a class, we usually refer to them as attributes.

Attributes describe our object, and functions are actions our object can take.

A class is more of a blueprint for making the object and the actual object created from
the class is called an instance of the class.  The process of when the class is creating
object is thereby called instantiation.

It is highly recommended to store your classes in modules to be imported for further use.
It is also highly recommended that every class name be camel cased, and that all classes
are immediately followed by comments regarding what the class does.

The format for creating classes is as follows.
'''


class Dog():
    # A programmers model of a dog
    def __init__(self, name, age):
        # Initializes the dog's attributes, like it's name and age
        self.name = name
        self.age = age

    def displayInfo(self):
        print ("Name: {0} \nAge: {1}".format(self.name, self.age))

    def sit(self):
        # Simulates the dog sitting
        print (self.name.title() + " is now sitting.")

    def roll_over(self):
        print (self.name.title() + " rolled over!")


'''
If you'll look on line 26, we used a special function or METHOD that runs whenever we're
creating instances.  It has a double underscore before and after the init to avoid conflict
with any method names you might include in your class.

You'll also see within the same line that the parameters for the __init__() method have
something called self.

So what is Self?  Well simply put, self is whatever instance you're creating.  You can see
that dot notation is being used to refer to an existing module within python, which is
why it doesn't have to be imported.  That module is the one python is using to create
the instance of the class and in order for it to create our objects for us, we have to
pass it self, along with any attributes we want for our instance.

After the arguments are passed, python access self.name and sets it equal to whatever name
you passed through.  The same follows for any attribute in a class.

Once again, you'll see self included in the parameters for our methods but that just allows
our methods to access our instances attributes, since they're part of self.
'''
