#                           How to use continue

'''
The usage of continue is somewhat similiar to break except instead of ending
the current loop, it just skips over whatever iteration it is currently on.
'''

list = list(range(1, 11))
for item in list:
    if item != 5:
        print (item)
    else:
        continue

'''
Below you'll see it skipped over the number five but continued afterwards.
I know, I know, break and continue are very self explanatory.
Results:
    1
    2
    3
    4
    6
    7
    8
    9
    10
'''
