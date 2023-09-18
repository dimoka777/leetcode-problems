# Bloomberg Amazon Adobe
# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example 1:

# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        ans = head.next
        while head and head.next:
            if prev:
                prev.next = head.next
            prev = head
            next_node = head.next.next
            head.next.next = head

            head.next = next_node
            head = head.next

        return ans
