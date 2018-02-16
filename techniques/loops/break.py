#                             How to use break

'''
You can use break to exit while loops or for loops which is why I put this in
loops.

Using 'break' ends whichever loop you're currently in
'''
list = list(range(1, 11))
for item in list:
    if item != 9:
        print (item)
    else:
        break

'''
If You see below, our list has numbers from 1 - 10, but our program breaks once
it hits a number that is equal to 9
Results:
    1
    2
    3
    4
    5
    6
    7
    8
'''
