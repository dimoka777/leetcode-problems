# Facebook Google Amazon
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Example 1:

# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def find_range(node):
            if low <= node.val <= high:
                nonlocal ans
                ans += node.val
            
            if node.left and node.val > low:
                find_range(node.left)
            
            if node.right and node.val < high:
                find_range(node.right)
        find_range(root)
        return ans
