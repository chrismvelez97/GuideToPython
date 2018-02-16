#                        How to let users quit an input()

'''
Sometimes you want a programt to keep running even if the user has entered a
response.

In these cases you need to give the user the ability to resign from the program
How to do so is laid out below
'''

prompt = "\nTell me somethign, and I will repeat it back at you "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print (message)

'''
In line 11 we provide a prompt for the user to see

In line 12 we add on another string in a new line informing them that they can
enter the command 'quit' to exit the program.

In line 13 we create an empty variable the program will use to repeat the users
entry back to them.

In line 14 we tell python to keep running the input() function as long as the
response is not to 'quit'

Line 15 runs the input() function with all the given prompts, and sets the
empty variable 'message' equal to whatever the user enters

Line 16 prints the 'message' and runs the while loop again if the message, is
not equal to 'quit'
'''
