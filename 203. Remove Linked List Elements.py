# Amazon Bloomberg Apple
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = res = ListNode(0, head)
        curr = ans.next
        while curr:
            if curr.val != val:
                ans.next = curr
                ans = ans.next
            curr = curr.next
        ans.next = None
        return res.next
