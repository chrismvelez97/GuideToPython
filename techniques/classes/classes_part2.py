from classes_part1 import Dog as d
# Above we import the dog class we created in part 1.

my_dog = d(name="California", age="10")

#   Here you can see our attribute executing perfectly
print (my_dog.name)
#   Results: California

#   Here you can see our method executing perfectly
my_dog.roll_over()
#   Results: California rolled over!


print (my_dog)
#   Results: <classes_part1.Dog object at 0x7fb233a40780>

'''
If you'll look above at our created object, when we print out our instance
of our dog class, it displays the module, the name of the class and lastly
a memory location of where the instance is stored.  For now, don't worry
to much about that memory location part.

The main point here is that although we have created our instance, when
we print it out it's not exactly human readable.

We can fix this but in order to do this we must create a method to read the
information.  Luckily we did this and we'll take avantage of that method in
the next couple of lines.
'''
my_dog.displayInfo()
'''
Results:
Name: California
Age: 10
'''
