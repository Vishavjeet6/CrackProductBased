160. Intersection of Two Linked Lists

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s1=[]
        s2=[]
        while headA:
            s1.append(headA)
            headA = headA.next
        while headB:
            s2.append(headB)
            headB = headB.next
        ans = None
        while s1!=[] and s2!=[]:
            a1 = s1.pop()
            a2 = s2.pop()
            if a1 == a2:
                ans = a1
            else:
                break
        return ans


# approach2
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getLengthAndTail(head):
            if head is None:
                return None,None
            s=1
            tail = head
            while(tail.next):
                tail = tail.next
                s += 1
            return (s,tail)
        la,ta = getLengthAndTail(headA)
        lb,tb = getLengthAndTail(headB)
        if la is None or lb is None:
            return None
        if ta != tb:
            return None
        pa=headA
        pb=headB
        if la > lb:
            s = la-lb
            while s:
                pa = pa.next
                s-=1
        elif la < lb:
            s = lb-la
            while s:
                pb = pb.next
                s-=1
        while pa != pb:
            pa=pa.next
            pb=pb.next
        return pa
            