import math

#operaters
#The ‘+’, ‘-’, ‘*’, ‘/’ operators perform a
#ddition, subtraction, multiplication and division respectively 
#on the top two items from the stack.
ops = {
  "+": (lambda a, b: a + b),
  "-": (lambda a, b: a - b),
  "*": (lambda a, b: a * b),
  "/": (lambda a, b: a / b),
  "sqrt":(lambda a: math.sqrt(a)),
  "clear":(),
  "undo":(),
}

#Recursion function: calculate
#maintain two stack structure, one for calculation, 
#the other for undo operate
def calculate(stack, undoStack, last_move):
    user_input = raw_input()
    tokens = user_input.split()
    stack = stack
    undoStack = undoStack
    last_move = last_move
    position = -1
    
    for token in tokens:
        position += 1
        if token in ops: 
            if token == 'sqrt':
                #detect insucient parameters
                if len(stack) < 1:
                    print 'operator ' + token + '(position: ' + str(position*2+1) + '):' + ' insucient parameters'
                    break
                else:
                    arg1 = stack.pop()
                    result = round(ops[token](arg1), 10)
                    undoStack.append(arg1)
                    stack.append(result)
                    last_move = 'calsqrt'
            elif token == 'clear':
                stack = []
            elif token == 'undo':
                if last_move == 'calsqrt':
                    stack = stack[:-1]
                    stack.append(undoStack.pop())
                elif last_move == 'cal':
                    stack = stack[:-1]
                    stack.append(undoStack.pop())
                    stack.append(undoStack.pop())
                elif last_move == 'append': 
                    stack = stack[:-1]
            else:  
                #detect insucient parameters
                if len(stack) < 2:
                    print 'operator ' + token + '(position: ' + str(position*2+1) + '):' + ' insucient parameters'
                    break
                else:
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    result = round(ops[token](arg1, arg2), 10)
                    undoStack.append(arg2)
                    undoStack.append(arg1)
                    stack.append(result)
                    last_move = 'cal'
        else:
            stack.append(int(token))
            last_move = 'append'
            undoStack.append(int(token))
  
    #format output string  
    strStack = ''
    for item in stack:
        if type(item) is float and (item).is_integer():
            item = int(item)
        strStack = strStack + ' ' + str(item)
        
    print 'stack:' + strStack
    calculate(stack, undoStack, last_move)
    return 
#---calculate function---end---