# 234. Palindrome Linked List

# o(n) space and time
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return 1
        l=[]
        while head:
            l.append(head.val)
            head = head.next
        i=0
        j=len(l)-1
        while i<=j:
            if l[i]!=l[j]:
                return 0
            else:
                i += 1
                j -= 1
        return 1

# approach 2
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return 1
        l=[]
        fast = head
        slow = head
        while fast and fast.next:
            l.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow:
            if l.pop() != slow.val:
                return 0
            slow = slow.next
        return 1
        