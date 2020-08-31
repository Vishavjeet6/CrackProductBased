class StackNode:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, item):
        temp = StackNode(item)
        temp.next = self.top
        self.top = temp
    
    def pop(self):
        if self.top is None:
            return
        item = self.top.data
        self.top = self.top.next
        return item
    
    def peek(self):
        if self.top is None:
            return
        return self.top.data
    
    def is_empty(self):
        return self.top is None


s = Stack()
print(s.is_empty())
s.push(1)
s.push(2)
print(s.peek())
s.push(3)
s.push(4)
print(s.pop())
