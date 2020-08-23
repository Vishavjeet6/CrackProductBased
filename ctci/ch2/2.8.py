#  o(n) space and time
def loop_detection(head):
    s = set()
    while 1:
        if head in s:
            return head
        s.add(head)
        head = head.next

#  book approach o(1) space o(n) time
def loop_detection(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    if fast is None or fast.next is None:
        return None
    slow = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return slow
