# Facebook Amazon Google
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 2


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def min_depth(node, ans):
            if not node:
                return float('inf')
            
            if not node.left and not node.right:
                return ans
            
            left = min_depth(node.left, ans + 1)
            right = min_depth(node.right, ans + 1)
            
            return min(left, right)
        
        if not root:
            return 0
            
        return min_depth(root, 1)
