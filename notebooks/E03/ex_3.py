# file: ex_3.py
# Lesson on Exceptions
'''
Demonstrates use of try-except to insure integer input
using multiple except clauses.
'''

# Repeat until the user enters an integer response
while True:
    try:
        age = input("Enter your age: ")
        age = int(age)
        break
    except ValueError:
        print("You entered '{}'.".format(age) +  
              "  You must enter a number for your age.")
    except EOFError:
        print("I think you forgot to enter a number for your age.")
    except KeyboardInterrupt:
        print("\nOUCH! Please don't terminate me.")
    print()

# The postcondition of the above code is that age is an integer

# The precondition of the following code is that age is an integer
# because the format of the string below requires it.
print('You reported your age as {:d} years.'.format(age))

input("Press ENTER to continue")