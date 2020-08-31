class QueueNode:
    def __init(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    
    def add(self, item):
        temp = QueueNode(item)
        if self.first is None:
            self.first = temp
        temp.next = last
        self.last = temp 