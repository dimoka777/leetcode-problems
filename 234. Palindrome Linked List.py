# Amazon Apple Adobe
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
 
# Example 1:

# Input: head = [1,2,2,1]
# Output: true


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        while prev and head and prev.val == head.val:
            prev = prev.next
            head = head.next
        
        return True if not prev else False
