# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c = 0
        s = l1.val + l2.val
        if s>9:
            s-=10
            c=1
        ans = ListNode(s)
        temp = ans
        l1 = l1.next
        l2 = l2.next
        while l1 or l2:
            if l1 is None:
                v1 = 0
            else:
                v1 = l1.val
            if l2 is None:
                v2 = 0
            else:
                v2 = l2.val
                
            s = v1 + v2 + c
            if s>9:
                c=1
                s -= 10
            else:
                c=0
            temp.next = ListNode(s)
            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if c==1:
            temp.next = ListNode(c)
        return ans
            
# recursive

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def addList(l1, l2, carry):
            if l1 is None and l2 is None and carry==0:
                return None
            value = carry
            if l1:
                value += l1.val
            if l2:
                value += l2.val
            nn = ListNode(value%10)
            if l1 or l2:
                mm = addList(None if l1 is None else l1.next, 
                             None if l2 is None else l2.next,
                             1 if value>9 else 0)
                nn.next = mm
            return nn
        return addList(l1, l2, 0)
        