class Queue:

    def __init__(self):
        self.queue = []
    
    def add(self, data):
        self.queue.append(data)
    
    def remove(self):
        if self.queue == []:
            return
        return self.queue.pop(0)
    
    def peek(self):
        if self.queue == []:
            return
        return self.queue[0]
    
    def is_empty(self):
        return self.queue == []
    
    def __str__(self):
        return str(self.queue)


q = Queue()
q.add(4)
q.add(3)
q.add(6)
print(q)
print(q.remove())
print(q)
print(q.peek())
print(q)
print(q.is_empty())
