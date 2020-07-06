def k_last(head, k):
    if head is None: 
        return
    size = 0
    temp = head 
    while(temp):
        size += 1
        temp = temp.next
    start = size - k
    temp = head 
    while(start > 0):
        temp = temp.next
        start -= 1
    return temp


def pushing(head, k):
    if head is None return
    pushing(head.next,k)

def poping(head, n, k):
    if n==k:
        return
    poping()



def k_last_recursive_client(head , k):
    if head is None:
        return
    pushing(head,k)
    poping(head,0,k)