#                           How to use elif statements

'''
The following code checks to see if the variable age is under four.
If it is, then that line of code will print.

If it is not true then it will go to the elif statement and check to see if age
is less than 18.

If all else fails than the else statement will run.  You may only have ONE if
statement and only ONE else statement but you may have multiple elif statements

Lastly, you may omit the else statement and just have the if and elif
statements
'''
ages = [1, 10, 21]
for age in ages:
    if age < 4:
        print ("Your admission cost is $0")
    elif age < 18:
        print ("Your admission cost is $5")
    else:
        print ("Your admission cost is $10")

'''
Results:
Your admission cost is $0
Your admission cost is $5
Your admission cost is $10
'''
