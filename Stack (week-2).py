class Stack:

    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1
 
    def push(self, val):
        if self.isFull():
            print('Stack Overflow! Calling exit().')
            exit(-1)
 
        print(f'Inserting {val} into the stack.')
        self.top = self.top + 1
        self.arr[self.top] = val

    def pop(self):
        if self.isEmpty():
            print('Stack Underflow! Calling exit().')
            exit(-1)
 
        print(f'Removing {self.peek()} from the stack.')
        top = self.arr[self.top]
        self.top = self.top - 1
        return top

    def peek(self):
        if self.isEmpty():
            exit(-1)
        return self.arr[self.top]

    def size(self):
        return self.top + 1

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity
  
if __name__ == '__main__':
 
    stack = Stack(3)
    stack.push(1)  
    stack.push(2)      
    stack.pop()        
    stack.pop()       
    stack.push(3)       
 
    print('Top element is: ', stack.peek())
    print('The stack size is: ', stack.size())
 
    if stack.isEmpty():
        print('The stack is empty.')
    else:
        print('The stack is not empty.')
        
        
        
'''OUTPUT:
Inserting 1 into the stack.
Inserting 2 into the stack.
Removing 2 from the stack.
Removing 1 from the stack.
Inserting 3 into the stack.
Top element is:  3
The stack size is:  1
The stack is not empty. '''
