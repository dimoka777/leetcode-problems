# Goldman Sachs Microsoft
# Given the head of a linked list, find all the values that appear more than once in the list and delete the nodes that have any of those values.

# Return the linked list after the deletions.

 
# Example 1:

# Input: head = [1,2,3,2]
# Output: [1,3]
# Explanation: 2 appears twice in the linked list, so all 2's should be deleted. After deleting all 2's, we are left with [1,3].

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        cnt = defaultdict(int)
        tmp = head
        while tmp:
            cnt[tmp.val] += 1
            tmp = tmp.next
        
        res = None
        while head:
            if cnt.get(head.val) == 1:
                if not res:
                    res = tmp = head
                else:
                    tmp.next = head
                    tmp = tmp.next
            head = head.next
        if tmp:
            tmp.next = None
        return res
