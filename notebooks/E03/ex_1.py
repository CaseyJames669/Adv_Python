# file: try_die.py
# Lesson on Exception Handling
'''
demonstrates more graceful termination on exception, but
not very friendly behavior
'''
from sys import exit

try:
    age = int(input('Enter your age: '))
except:
    print("Sorry.  Your input must be numeric.")
    input("Press ENTER to continue")
    exit()
# Postcondition of this code segment is "age is integer"

# Precondition of following code is "age is integer"
print('Your entered age is {:d} years.'.format(age))

input("Press ENTER to continue")