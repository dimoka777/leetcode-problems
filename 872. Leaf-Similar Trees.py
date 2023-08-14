# Google
# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# For exemple, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Example 1:

# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true

class Solution:
    
    @staticmethod
    def check_leafs(head, res):
        stack = [head]
        while stack:
            node = stack.pop()
            if not node.right and not node.left:
                res.append(node.val)
                continue

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.check_leafs(root1, []) == self.check_leafs(root2, [])
