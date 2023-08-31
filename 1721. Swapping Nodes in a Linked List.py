# Adobe Amazon Facebook 
# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt = 0
        curr = head
        first = None
        last = None
        while curr:
            cnt += 1
            if last:
                last = last.next
            if cnt == k:
                last = head
                first = curr
            curr = curr.next
        first.val, last.val = last.val, first.val
        return head
