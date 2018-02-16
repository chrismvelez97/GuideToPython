#                   How to use arguments and parameters

'''
Previously we talked about how to define functions, but the one we created
had no parameters, meaning that it didn't need any extra information to do it's
job.  When a function does need information to do it's job it will have
parameters, and you fill these parameters with arguments.

You can have multiple parameters and you can even have it so that the extra
parameters are optional
'''


def greet_user(username):
    print ("Hello {0}!".format(username))


#   Ex.1
greet_user("Chris")
#   results: Hello Chris!

#   Ex.2
greet_user("Joe")
#   results: Hello Joe!
