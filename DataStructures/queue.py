class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


myQueue = Queue()

for char in (input()):
    myQueue.enqueue(char)

for i in range(0,myQueue.size()):
    print(myQueue.dequeue())

