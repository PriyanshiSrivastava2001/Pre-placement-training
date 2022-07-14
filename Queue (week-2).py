class Queue:
    def __init__(self, size=1000):
        self.q = [None] * size      
        self.capacity = size       
        self.front = 0              
        self.rear = -1              
        self.count = 0              

    def dequeue(self):
        if self.isEmpty():
            print('Queue Underflow! Terminating process.')
            exit(-1)
        x = self.q[self.front]
        print('Removing element...', x)
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1
        return x

    def enqueue(self, value):
        if self.isFull():
            print('Overflow! Terminating process.')
            exit(-1)
        print('Inserting element...', value)
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1

    def peek(self):
        if self.isEmpty():
            print('Queue UnderFlow! Terminating process.')
            exit(-1)
        return self.q[self.front]

    def size(self):
        return self.count

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity
 
if __name__ == '__main__':

    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
 
    print('The queue size is:', q.size())
    print('The front element is:', q.peek())
    q.dequeue()
    print('The front element is:', q.peek())
 
    q.dequeue()
    q.dequeue()
 
    if q.isEmpty():
        print('The queue is empty.')
    else:
        print('The queue is not empty.')
        
        
''' OUTPUT-
Inserting element... 1
Inserting element... 2
Inserting element... 3
The queue size is: 3
The front element is: 1
Removing element... 1
The front element is: 2
Removing element... 2
Removing element... 3
The queue is empty. '''
