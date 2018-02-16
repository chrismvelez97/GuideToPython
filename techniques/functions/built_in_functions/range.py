#                           How to use range in python

'''
So after looking over this I really debated with myself if I should
put this under method or techniques and I ended up putting it here because,
the function doesn't execute if not in conjunction with a for loop, hence it
being a technique.

The range(start, end) function creates a set of numbers to
generate starting at the first argument, and ending BEFORE the last argument.
This means that if you put range(1:5) it will go from 1 to 4, not 1 to 5.

Also, if you only enter one argument into the range() function, it will start
at 0 and continue until right before whatever number you entered.

Lastly, you can also use range to generate only even numbers or odd numbers.
(see ex.3-4)
'''

#   Ex.1
for value in range(1, 5):
    print(value)

'''
Note that below the result aren't inline as each new line is a new result
Results:
1,
2,
3,
4,
'''

#   Ex.2
print ("\n ")
for value in range(5):
    print (value)
print ("\n")
'''
Note that below the result aren't inline as each new line is a new result
Results:
0,
1,
2,
3,
4,
'''

#   Ex. 3
print("Odds:")
for value in range(1, 11, 2):  # You must start with an odd number to do odds
    print (value)

print("\n")

'''
Note that instead this third argument adds by two giving us only odd
numbers.
Results:
1,
3,
5
'''

#   Ex. 4
print ("Evens:")
for value in range(2, 11, 2):  # You must start with an even number to do evens
    print (value)
print ("\n")
