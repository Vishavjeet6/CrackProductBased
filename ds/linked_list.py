class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get_size(self):
        print(self.size)
        return self.size
    
    def add_last(self, data):
        self.size += 1
        if self.head is None:
            self.head = Node(data)
            return
        else:
            temp = Node(data)
            temp_start = self.head
            while(temp_start.next):
                temp_start = temp_start.next
            temp_start.next = temp
    
    def add_first(self, data):
        self.size += 1
        if self.head is None:
            self.head = Node(data)
            return
        else:
            new_head = Node(data)
            new_head.next = self.head
            self.head = new_head
    
    def add_after(self, node, data):
        if self.head is None:
            return
        self.size += 1
        temp = self.head
        while(temp):
            if temp.data == node:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            else:
                temp = temp.next
        else:
            print("Node not found")

    def print_list(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while(temp):
                print(temp.data, sep = " ", end = " ")
                temp = temp.next
            print()
    
    def remove_first(self):
        if self.head is None:
            return
        self.size -= 1
        self.head = self.head.next    
    
    def remove_last(self):
        if self.head is None:
            return
        self.size -= 1     
        if(self.head.next is None):
            self.head = None
            return
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        temp.next = None
        return
    
    def remove_inbetween(self, node):
        if self.head is None:
            return
        # self.size -= 1
        if self.head.data == node:
            self.head = self.head.next
            self.size -= 1
            return
        prev = self.head
        curr = self.head.next
        while(curr):
            if curr.data == node:
                prev.next = curr.next
                self.size -= 1
                return
            else:
                prev = curr
                curr = curr.next
        print("Node not found")

        
        
ll = LinkedList()
ll.add_last(1)
ll.add_last(2)
ll.add_last(3)
ll.add_last(4)
ll.print_list()
ll.get_size()
ll.add_first(6)
ll.add_after(6,5)
ll.print_list()
ll.get_size()
ll.remove_inbetween(5)
ll.print_list()
ll.get_size()
ll.remove_inbetween(9)
ll.print_list()
ll.get_size()
ll.remove_first()
ll.print_list()
ll.get_size()
ll.remove_last()
ll.print_list()
ll.get_size()