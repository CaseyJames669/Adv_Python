names = ['bert', 'ernie', 'arne', 'oscar']

# emulate "for name in names:"
# temp is our temporary "internal" iterator
temp = iter(names)          # create an iterator over our iterable
while True:
    try:
        name = next(temp)   # get the 'next' value from the iterator
    except StopIteration:  # got to the end of the iterator's stream
        del temp           # we no longer need the exhausted iterator
        break              # exit loop
    # loop body goes here
    print(name)
        