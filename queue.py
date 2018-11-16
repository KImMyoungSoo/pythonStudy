class queue :
    def __init__(self):
        self.queue = []
    def put(self,obj):
        self.queue.append(obj)
        self.queue.sort(reverse = True)
    def getItem(self) :
        item = self.queue[0]
        del(self.queue[0])
        return item
    def printQueue(self) :
        for i in self.queue :
            print(i, end=' ')

q = queue()

q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
q.printQueue()
item = q.getItem()
print()
print(item)
q.printQueue()
item = q.getItem()
print()
print(item)
q.printQueue()
