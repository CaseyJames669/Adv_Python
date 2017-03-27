# file: ex_2.py
# Lesson on Exception Handling
# demonstrates a more friendly input error handling

while True:
    try:
        age = int(input('Enter your age: '))
        break
    except:
        print("\nSorry.  Your input must be numeric.  Please re-enter.")
# Postcondition of the above code segment is "age is integer"

# Precondition of following code is "age is integer"
print('\nYour entered age is {:d} years.'.format(age))

input("Press Enter to continue ")