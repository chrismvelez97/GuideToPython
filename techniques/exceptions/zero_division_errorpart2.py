#                      How to handle the Zero Division Error

'''
Below, we'll use create a calculator
that can only handle division operations.

This is to simulate how we want to use
exceptions to allow our program to
continue in case of failures.
'''
print ("If give me two numbers, I'll divide them for you.\nEnter 'q' to quit.")

while True:
    f_num = input("\nFirst Number: ")
    if f_num == 'q':
        break
    sec_num = input("Second Number: ")
    if sec_num == 'q':
        break
    try:
        answser = int(f_num) / int(sec_num)
    except ZeroDivisionError:
        print ("\nYou cannot divide by 0.\nPlease try again or press 'q' to quit")
    else:
        print (answser)
