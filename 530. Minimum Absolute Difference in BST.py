# Facebook Google Amazon
# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

# Example 1:

# Input: root = [4,2,6,1,3]
# Output: 1

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        def get_array(node):
            if node.left:
                get_array(node.left)
            nonlocal values
            values.append(node.val)
            if node.right:
                get_array(node.right)
        get_array(root)
        dif = float('inf')
        for i in range(1, len(values)):
            dif = min(dif, values[i] - values[i - 1])
        return dif
