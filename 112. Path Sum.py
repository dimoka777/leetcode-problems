# Facebook Bloomberg Google
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Example 1:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.


class Solution:
    def __init__(self):
        self.target = None

    def rec(self, tmp, total):
        if not tmp:
            return False

        total += tmp.val
        if not tmp.left and not tmp.right:
            return total == self.target

        left = self.rec(tmp.left, total)
        right = self.rec(tmp.right, total)
        return left or right
        
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.target = targetSum
        return self.rec(root, 0)
