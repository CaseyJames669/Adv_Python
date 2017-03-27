# file: collect.py
# author: Rick
# CSIS 153 - Asmt 4

''' Implementations of the Stack and Queue data structures'''


class Stack:
    '''Stack() -> new empty Stack object
    
    The Stack is a linear structure having LIFO(Last In - First Out) access
    '''
    
    def __init__(self):
        '''Constructor'''
        
        self._data = []
        
    def push(self, item):
        '''Put 'item' at top of Stack
        
        Precondition: a data item must be provided
        Postcondition: 'item' is placed at the top of the Stack;
                        no value is returned;
                        state of the Stack is changed
        '''
        
        self._data.append(item)
        
    def pop(self):
        '''Remove and return the value at the top of the Stack
        
        Precondition: Stack must not be empty
        Postcondition: The item at the top of the Stack is removed and
                       its value is returned as the value of the function;
                       state of the Stack is changed;
                       If Stack is empty, raises the IndexError exception
        '''
        return self._data.pop()
        
    def clear(self):
        '''Remove all items from Stack
        
        Precondition:  None
        Postcondition:  The Stack is empty
        '''
        self._data = []
        
    def is_empty(self):
        '''True if Stack is empty
        
        Precondition: None
        Postcondition: Returns True if Stack is empty, else False;
                       state of Stack is unaltered
        '''
        return len(self._data) == 0
        
    def top(self):
        '''Return the value of the item at top of Stack
        
        Purpose:  Returns the value of the item at the top of the Stack
                  without removing it from the Stack
        Precondition:  Stack is not empty
        Postcondition:  Return the item at the top of the stack;
                        If Stack is empty, raises the IndexError exception;
                        state of Stack is not altered
        '''
        
        return self._data[len(self._data) -1]
        
    def __len__(self):
        '''Return the size of the Stack
        
        Precondition: None
        Postcondition:  Returns the number of items on the Stack;
                        state of Stack is unaltered
        '''
        return len(self._data)
        
    def __eq__(self, other):
        '''Answer stack1 == stack2
        
        Precondition:  'other' is a Stack
        Postcondition:  
            Returns True if Stacks contain the equal items
            in the same order; False otherwise
            Stack is unaltered
        
        '''
        return self._data == other._data
               
    def __str__(self):
        '''Create a string (str) representation of the Stack
        
        Precondition:  None
        Postcondition:  Returns a string reporting the contents of the Stack
                        with the top item on the left, signified with '->';
                        state of Stack is unaltered
        '''
        return '<' + str(self._data)[1:-1] + '>'

        
class Queue:
    '''Queue() -> new empty Queue object
    
    The Queue is a linear structure having FIFO(Last In - First Out) access
    '''
    
    def __init__(self, arg = None):
        '''Constructor'''
        if arg:
            self._data = list(arg)
        else:
            self._data = []
    
    def enque(self, item):
        '''Add item to the end of the Queue
            
            Precondition:  an item to enque is supplied
            Postcondition:  item is added to the end of the queue;
                            state of Queue is altered
        '''
        self._data.append(item)
        
    def deque(self):
        '''Remove and return the item at the front of the Queue
        
        Precondition:  The Queue cannot be empty
        Postcondition:  The item a the front of the Queue is removed and its
                        value is returned as the value of the method;
                        Queue is altered;
                        If the Queue is empty, IndexError exception is raised
        '''
        return self._data.pop(0)

    def clear(self):
        '''Remove all items from Queue
        
        Precondition:  None
        Postcondition:  The Queue is empty
        '''
        self._data = []
        
    def is_empty(self):
        '''True if Queue is empty
        
        Precondition: None
        Postcondition: Returns True if Queue is empty, else False;
                       state of Queue is unaltered
        '''
        return len(self._data) == 0
        
    def front(self):
        '''Return the value of the item at front of the Queue
        
        Purpose:  Returns the value of the item at the front of the Queue
                  without removing it from the Queue
        Precondition:  Queue is not empty
        Postcondition:  Return the item at the front of the Queue;
                        If Queue is empty, raises the IndexError exception;
                        state of Queue is not altered
        '''
        
        return self._data[0]
        
    def __len__(self):
        '''Return the size of the Queue
        
        Precondition: None
        Postcondition:  Returns the number of items in the Queue;
                        state of Queue is unaltered
        '''
        return len(self._data)
        
    def __eq__(self, other):
        '''Answer queue1 == queue2
        
        Precondition:  'other' is a Queue
        Postcondition:  
            Returns True if Queues contain the equal items
            in the same order; False otherwise
            Queue is unaltered
        
        '''
        return self._data == other._data
       
    def __str__(self):
        '''Create a string (str) representation of the Queue
        
        Precondition:  None
        Postcondition:  Returns a string reporting the contents of the Queue
                        with the front item on the left, signified with '<<<';
                        state of Queue is unaltered
        '''
        return '<' + str(self._data)[1:-1] + '>'

    
if __name__ == '__main__':
    print("******STACK TEST******")
    s = Stack()
    print("length of a new Stack is ", len(s))
    print("new Stack is empty? ", s.is_empty())
    print("Push 'a', then 'butter', then [1, 2, 'three'] onto Stack")
    s.push('a'), s.push('butter'), s.push([1, 2, 'three'])
    print("There are", len(s), "items on the Stack")
    print("The Stack is:  ", s)
    print("The item at the top of the Stack is: '" + str(s.top()) + "'")
    print("Is the Stack is empty? ", s.is_empty())
    print("Empty the Stack, one item at a time:")
    while not s.is_empty():
        print("Remove and report the item at the top of the Stack:")
        print("\tJust popped the item:", s.pop())
        print("\tThe Stack is now:  ", s)
    print ("Push 'a', then 'butter', then [1, 2, 'three'] onto Stack")
    s.push('a'), s.push('butter'), s.push([1, 2, 'three'])
    print("The Stack is:  ", s)
    print("Clear the stack with 'clear' method")
    s.clear()
    print("The Stack is:  ", s)
    
    
    print("\n******Queue TEST******")
    s = Queue()
    print("length of a new Queue is ", len(s))
    print("new Queue is empty? ", s.is_empty())
    print("Enque 'a', then 'butter', then [1, 2, 'three'] onto Queue")
    s.enque('a'), s.enque('butter'), s.enque([1, 2, 'three'])
    print("There are", len(s), "items on the Queue")
    print("The Queue is:  ", s)
    print("The item at the front of the Queue is: '" + str(s.front()) + "'")
    print("Is the Queue is empty? ", s.is_empty())
    print("Empty the Queue, one item at a time:")
    while not s.is_empty():
        print("Remove and report the item at the front of the Queue:")
        print("\tJust deque'd the item:", s.deque())
        print("\tThe Queue is now:  ", s)
    print ("Enque 'a', then 'butter', then [1, 2, 'three'] onto Queue")
    s.enque('a'), s.enque('butter'), s.enque([1, 2, 'three'])
    print("The Queue is:  ", s)
    print("Clear the Queue with 'clear' method")
    s.clear()
    print("The Queue is:  ", s)
