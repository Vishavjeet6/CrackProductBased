def partition(head, k):
    if head in None:
        return
    temp = head
    size = 1
    while temp.next:
        temp = temp.next
        size += 1
    tail = temp
    prev = head
    start = head.next
    counter = 0
    if head.data >= k:
        tail.next = head
        head = head.next
        tail = tail.next
    while(counter < size and start is not None):
        if start.data >= k:
            tail.next = start
            prev.next = start.next
            tail = tail.next
        counter += 1

# book approach
def partition(head, k):
    ll_head = head
    ll_tail = head
    temp = head
    while(temp):
        if temp.data < k:
            temp.next = ll_head
            ll_head = temp
        else:
            ll_tail.next = temp
            ll_tail = temp
        temp = temp.next
    ll_tail.next = None
    return ll_head
