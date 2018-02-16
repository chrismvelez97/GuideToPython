#                           How to use flags

'''
Okay so for this file I didn't know if I should include it in input() or in
techniques in general.

The reason for this is the fact that it seems to be specifically useful for
programs involving the input() function.

The reason I decided to include it in the general area of the techniques folder
is because although it is useful for using in conjunctino with the input()
function it can really be used with anything else.

Despite this, I will be using it in conjunction with the input() function below
'''

prompt = "\nTell me something, and I will repeat it back at you "
prompt += "\nEnter 'quit' to end the program. "
message = ""

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print (message)

'''
If you examine this code you can see that it is similiar to the code in the
input folder inside the user_quit.py file.

This is because I copied and pasted.

If you'll notice the only difference was that we moved the conditional inside
of the while loop and said if this conditional is true than set active to False
thereby ending the program.

Before that, we set the conditional we wanted the while loop to check for to
check the value of active which is alway true unless we enter 'quit'
'''
