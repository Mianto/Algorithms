class Heap:
    def __init__(self):
        self.capacity = 10
        self.items = [0]*self.capacity
        self.size = 0

    def getLeftChildIndex(self, parentIndex):
        return 2*parentIndex+1
    def getRightChildIndex(self, parentIndex):
        return 2*parentIndex+2
    def getParentIndex(self, childIndex):
        return (childIndex-1)/2

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) <= self.size
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) <= self.size
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def leftChild(self, index):
        return self.items[self.getLeftChildIndex(index)]
    def rightChild(self, index):
        return self.items[self.getRightChildIndex(index)]
    def parent(self, index):
        return self.items[self.getParentIndex(index)]

    def swap(self, index1, index2):
        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

    def pull(self): # give minimum element in the heap
        if self.size <= 0:
            return False
        return self.items[0]

    def poll(self): # remove the root element
        if self.size <= 0:
            return False
        item = self.items[0]
        self.items[0] = self.items[self.size-1]
        self.size -= 1
        self.heapifyDown()
        return item

    def insert(self, item):
        self.ensureExtraCapacity()
        self.items[self.size] = item
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size-1
        while self.hasParent(index) and self.parent(index)>self.items[index]:
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)


    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.leftChild(index) > self.rightChild(index):
                smallerChildIndex = self.getRightChildIndex(index)

            if self.items[index] < self.items[smallerChildIndex]:
                break
            else:
                self.swap(smallerChildIndex, index)
            index = smallerChildIndex

    def ensureExtraCapacity(self):
        if self.capacity == self.size + 1:
            self.capacity *= 2
            for i in xrange(self.capacity):
                self.items.append(0)


def main():
    h = Heap()
    a = [2, 5, 6, 9, 12]
    for x in a:
        h.insert(x)
    print h.poll()

if __name__ == '__main__':
    main()
