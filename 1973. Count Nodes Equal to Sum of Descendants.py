# Facebook
# Given the root of a binary tree, return the number of nodes where the value of the node is equal to the sum of the values of its descendants.

# A descendant of a node x is any node that is on the path from node x to some leaf node. 
# The sum is considered to be 0 if the node has no descendants.
 
# Example 1:

# Input: root = [10,3,4,2,1]
# Output: 2
# Explanation:
# For the node with value 10: The sum of its descendants is 3+4+2+1 = 10.
# For the node with value 3: The sum of its descendants is 2+1 = 3.


class Solution:
    def __init__(self):
        self.res = 0

    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            cnt = dfs(node.left) + dfs(node.right)
            if cnt == node.val:
                self.res += 1
            return cnt + node.val

        dfs(root)
        return self.res
