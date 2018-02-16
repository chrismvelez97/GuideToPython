#                        How to use the the input() function

'''
The input() function pauses the program and waits for a user to enter some text

It takes in one argument and that is the prompt which tells the user what is
expected of them.

The input() function converts everything to strings so if you're prompting the
user for a numerical input that you'd like to use as a number you should use
the int() method.

I decided to put the guide for input in techniques because it is not a method
attached to anything its just a standalone function.
'''
name = input("Hello! What is your name? ")

print ("\nHello {0}! It's very nice to meet you!".format(name))
