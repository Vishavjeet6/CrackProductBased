def remove_duplicate_unsorted(head):
    if head is None:
        return 
    d = {}
    prev = head
    curr = head.next
    d[prev.data] = 0
    while(curr):
        if curr.data in d.keys():
            temp = prev
            prev = curr
            temp.next = curr.next
            curr = curr.next
        else:
            d[curr.data] = 0
            prev = curr
            curr = curr.next


