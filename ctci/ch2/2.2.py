# recursive
def pushing(head):
    if head is None:
        return []
    temp = head
    stack = []
    while(temp):
        stack.append(temp)
        temp = temp.next
    return stack

def poping(s, kl):
    if kl==1:
        return s.pop()
    s.pop()
    return poping(s, kl-1)

def k_last_recursive_client(head, k):
    if head is None:
        return
    stack = pushing(head)
    k_last = popping(stack, k)
    print(k_last)


# iterative
def k_last_iterative_client(head, k):
    p1 = head
    p2 = head
    i=0
    while(i < k):
        p2 = head.next
    while p2:
        p1 = p1.next
        p2 = p2.next
    print(p1.data)
