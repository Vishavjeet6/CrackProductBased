class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if self.stack == []:
            return
        return self.stack.pop()

    def peek(self):
        if self.stack == []:
            return
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []
    
    def __str__(self):
        return str(self.stack)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s)
s.pop()
print(s)
print(s.peek())
print(s.is_empty())
print(s)
    