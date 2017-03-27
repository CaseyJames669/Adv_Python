# file: word.py
# author: Rick
# First part of Search Engine assignment

'''
This module contains functions for processing ITERABLES OF STRINGS containing
multiple white-space separated words.  
The functions are designed to produce words and word statistics from the
iterable.  
Though any iterable of this type can be processed, the primary input structure
of interest is a text file.  
'''

import string
 
def word_strip(wd):
    '''Strip string and return lowercase version of result
  
    Return a stripped, lowercase version of the word. A stripped word is one 
    that begins and ends with an alphabetic character and has no intervening 
    white space.  I.e. the input parameter has all non-alphabetic symbols 
    stripped away from its boundaries, but such symbols remaining in the
    interior of a word.
  
    Precondition: w is a string
    Postcondition: returns 'stripped' string in lowercase
    '''
    
    # non-letter printable characters
    clipper = ''.join([ch for ch in string.printable\
                                    if ch not in string.ascii_letters])
    return wd.strip(clipper).lower()

def words(data=None):
    '''Return an iterator over data that returns tuples of (line, word)
    
    Preconditions:  'data' must be an iterable of strings
    Postcondition:  returns an iterator over data that produces a tuple
                    (i, w) where:
                        w is the stripped lower-case representation of next
                            word in data and
                        i is the index of the item in data from which the 
                            word w was retrieved.
                    A stripped word is one that begins and ends with an 
                    alphabetic character and has no intervening white space.
    '''
    
    # iterate over the numbered strings in data
    for num, line in enumerate(data):
        # iterate over the stripped words in the current string
        for word in [word_strip(m_word) for m_word in line.split()]:
            # ignore empty words
            if word:
                yield(num, word)
            
def word_set(data):
    '''Return a sorted list of words that occur in data
    
    Precondition:  data must be an iterable of strings
    Postcondition: returns a list of white-space separated words that 
                   appear in data, with no duplicates.  
                   Words are lower case and list is sorted in 
                   increasing alphabetical order.
    '''
    
    wd_set = {word for num, word in words(data)}
    return sorted(wd_set)

def word_freq(data):
    '''Return a dict of {word:frequency} of words in data
    
    Precondition:  data must be an iterable of strings
    Postcondition:  returns a dict of {word:frequency} where
                    word is a lower case representation of a word 
                    from data and frequency is the word's frequency
                    of occurance in data
                    
    '''
    
    wd_freq = dict()
    # iterate over all stripped words in data
    for num, word in words(data):
        # if word already in dict, increment freq
        if word in wd_freq:
            wd_freq[word] += 1
        # otherwise add to dict with freq = 1
        else:
            wd_freq[word] = 1
            
    return wd_freq

def word_lines(data):
    '''Return a dict of {word:locations} of words in data
    
    Precondition:  data must be an iterable of strings
    Postcondition:  returns a dict of {word:locations} where
                    word is a lower case representation of a word 
                    from data and locations is a list of indices
                    from the data indicating each item in data that
                    contains word.  Each index occurs only once in
                    any given list.
    '''
    
    wd_line = dict()
    # iterate over all stripped words in data and the line they are on
    for line, word in words(data):
        # if the word is already in the dict
        if word in wd_line:
            # if this line isn't in the line list for word, add it
            if wd_line[word][-1] != line:
                wd_line[word].append(line)
        # otherwise, add the word to the dict and add the line to its list
        else:
            wd_line[word] = [line]
    return wd_line


if __name__ == '__main__':
    print("use word_strip on '2389jack's-o-lantern%^$#':")
    print(word_strip("2389jack's-o-lantern%^$#"))
    
    test_data = ['This is a line!', 
                 'but ... it is not just any #(*!^line*@',
                 'it is a line that is longer than other any other line']
    print("\nThis is the test data:\n", test_data)
    
    print('\nThis should be the words and line numbers in test_data:')
    for word_data in words(test_data):
        print(word_data)
    
    print('\nThis should be an alphabetized list of words for test_data:')
    print(word_set(test_data))
    
    print('\nThis should be a dict of {word:freq} of words in test_data:')
    print(word_freq(test_data))
    
    print('\nThis is a dict of {word:line_nums} of words in test_data:')
    print(word_lines(test_data))
