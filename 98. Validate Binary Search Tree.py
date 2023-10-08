# Yandex SIG Amazon
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 
# Example 1:

# Input: root = [2,1,3]
# Output: true


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid_bst(node, s, l):
            if not node:
                return True
            if not(s < node.val < l):
                return False
            left = valid_bst(node.left, s, node.val)
            right = valid_bst(node.right, node.val, l)
            return left and right
        return valid_bst(root, float('-inf'), float('inf'))
