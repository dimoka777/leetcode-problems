# Facebook Amazon Bloomberg
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0
        def long_path(node):
            if not node:
                return 0
            nonlocal diam
            left = long_path(node.left)
            right = long_path(node.right)
            diam = max(diam, left + right)
            return max(left, right) + 1
        long_path(root)
        return diam
