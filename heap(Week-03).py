import sys
class minheap:
    def __init__(self, size):
        self.storage=[0]*size
        self.size = size
        self.heap_size = 0
        self.Heap = [0]*(self.size + 1)
        self.Heap[0] = sys.maxsize * -1
        self.parent = 1
        self.root=1
    def getParentIndex(self,index):
        return (index-1)//2
    def getLeftChildIndex(self,index):
        return 2*index+1
    def getRightChildIndex(self,index):
        return 2*index+2
    def hasParent(self,index):
        return self.getParentIndex(index)>=0
    def insert(self,index):
        if self.heap_size >= self.size :
            return
        self.heap_size+= 1
        self.Heap[self.heap_size] = index
        heap = self.heap_size
        while self.Heap[heap] < self.Heap[heap//2]:
            self.swap(heap, heap//2)
            heap = heap//2
    def swap(self, left, right):
        self.Heap[left], self.Heap[right] = self.Heap[right], self.Heap[left]
    def root_node(self, i):
        if not (i >= (self.heap_size//2) and i <= self.heap_size):
            if (self.Heap[i] > self.Heap[2 * i]  or  self.Heap[i] > self.Heap[(2 * i) + 1]):
                if self.Heap[2 * i] < self.Heap[(2 * i) + 1]:
                    self.swap(i, 2 * i)
                    self.root_node(2 * i)
                else:
                    self.swap(i, (2 * i) + 1)
                    self.min_heapify((2 * i) + 1)
    def getMin(self):
        min_value = self.Heap[self.root]
        self.Heap[self.root] = self.Heap[self.root]
        self.size-= 1
        self.root_node(self.root)
        return min_value
    def extractMin(self):
        data=self.Heap[1]
        self.Heap[1]=self.Heap[self.size-1]
        self.size-=1
        return data
    def main(self):
       for i in range(1, (self.heap_size//2)+1):
            print("Parent Node:",str(self.Heap[i]),"Left Node:"+str(self.Heap[2 * i]),"Right Node:",str(self.Heap[2 * i + 1]))
minHeap = minheap(11)
minHeap.insert(70)
minHeap.insert(8)
minHeap.insert(80)
minHeap.insert(3)
minHeap.insert(90)
minHeap.insert(30)
minHeap.insert(23)
minHeap.insert(45)
minHeap.insert(100)
print("The Root element is" ,(minHeap.getMin()))
minHeap.main()
print("Remove node", minHeap.extractMin())
minHeap.main()



'''OUTPUT-
The Root element is 3
Parent Node: 3 Left Node:8 Right Node: 23
Parent Node: 8 Left Node:45 Right Node: 90
Parent Node: 23 Left Node:80 Right Node: 30
Parent Node: 45 Left Node:70 Right Node: 100
Remove node 3
Parent Node: 100 Left Node:8 Right Node: 23
Parent Node: 8 Left Node:45 Right Node: 90
Parent Node: 23 Left Node:80 Right Node: 30
Parent Node: 45 Left Node:70 Right Node: 100
'''
