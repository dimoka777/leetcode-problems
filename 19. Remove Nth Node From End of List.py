# Amazon Google Apple
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
 
# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        while n:
            fast = fast.next
            n -= 1
        
        if fast:
            while fast:
                fast = fast.next
                prev = slow
                slow = slow.next
        else:
            return head.next

        prev.next = slow.next
        
        return head
