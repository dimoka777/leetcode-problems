# Amazon Facebook Apple 
# Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

# A subtree of a node node is node plus every node that is a descendant of node.

 
# Example 1:

# Input: root = [1,null,0,0,1]
# Output: [1,null,0,null,1]
# Explanation: 
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)

            if not left:
                node.left = None
            
            if not right:
                node.right = None

            return node.val or left or right

        return root if dfs(root) else None
