# file: expression.py
# author: Rick

'''
Contains functions to evaluate postfix and infix expressions with
the operators +, -, *, /, and ^ for add, subtract, multiply, divide,
and exponentiation, resp.
'''

from collect import Stack, Queue

ops = {'+' : (10, 'L'),
       '-' : (10, 'L'),
       '*' : (20, 'L'),
       '/' : (20, 'L'),
       '^' : (30, 'R')
      }


def in2post(expr):
    '''Translate expr from infix to postfix notation
    
    Precondition: expr is a valid  infix expression with all
                  'tokens' separated by white space
    Postcondition: returns a white space separated string of 
                   'tokens' that is an equivalent postfix representation.
                   returns None if an the expression is invalid
    '''
    
    # covert the input expression into a Queue object
    tokens = Queue(expr.split())
    
    # create necessary data structures
    postout = Queue()
    opstack = Stack()
    
    # process the input tokens in order
    while not tokens.is_empty():
        token = tokens.deque()
        # is token an operator?
        if token in ops:
            while not opstack.is_empty() and opstack.top() in ops and \
                        (ops[token][1] == 'L' and \
                         ops[token][0] == ops[opstack.top()][0] or \
                         ops[token][0] < ops[opstack.top()][0]):
                
                postout.enque(opstack.pop())
            opstack.push(token)
        # is token a left paren?
        elif token == '(':
            opstack.push(token)
        # is token a right paren?
        elif token == ')':
            try:
                while opstack.top() != '(':
                    postout.enque(opstack.pop())
                opstack.pop()
            except:
                return None
        # token must be a number
        else:
            # if not a number, error out
            try:
                float(token)
            except:
                return None
            postout.enque(token)
    
    #dump the remainder of the operator stack to the output queue
    while not opstack.is_empty():
        if opstack.top() == '(':
            return None
        postout.enque(opstack.pop())
    
    # return the string representation of the postfix notation
    outlist = []
    while not postout.is_empty():
        outlist.append(postout.deque())
    return ' '.join(outlist)

def _evaluate(op1, op2, oper):
    if oper == '^':
        oper = '**'
    return eval(op1 + oper + op2)
    
def eval_postfix(expr):
    '''Evaluate the postfix expression and return a float value
    
    Precondition: expr is a valid postfix expression with all tokens
                  separated by while space
    Postcondition: returns the floating point value of the expression
                   returns None if the expression contains invalid token or
                   will return None or raise IndexError if ill-formed
    '''
    
    # covert the input expression into a Queue object
    tokens = Queue(expr.split())
    # create an operand stack
    opstack = Stack()
    
    while not tokens.is_empty():
        token = tokens.deque()
        if token in ops:
            op2, op1 = opstack.pop(), opstack.pop()
            opstack.push(str(_evaluate(op1, op2, token)))
        else:
            # do this to protect against executing arbitrary code with 'eval'
            try:
                float(token)
            except:
                return None
            opstack.push(token)
    
    # get and return result if valid, else None
    result = float(opstack.pop())
    if opstack.is_empty():
        return result
    else:
        return None
    
            
def eval_infix(expr):
    '''Evaluate the infix expression and return a float value
    
    Precondition:  expr must be a valid infix expression with all tokens
                   separated by white space.
    Postcondition: returns the floating point value of the expression
                   returns None if the expression is not valid.
    '''
    retval = in2post(expr)
    if retval:
        return eval_postfix(retval)
    else:
        return None

if __name__ == '__main__':
    expr = input("Enter an expressions to translate (empty to quit): ")
    while expr:
        print('Input string:  ', expr)
        post_expr = in2post(expr)
        print('Output string: ', post_expr)
        if post_expr:
            print('The value is: ', eval_postfix(post_expr))
        print('Directly computed value: ', eval_infix(expr))
        expr = input("Enter an expressions to translate (empty to quit): ")