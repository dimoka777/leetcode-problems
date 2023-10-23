# 513. Find Bottom Left Tree Value
# Medium 
# Amazon Yahoo Apple
# Given the root of a binary tree, return the leftmost value in the last row of the tree.

# Example 1:

# Input: root = [2,1,3]
# Output: 1


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ans = None
        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                if i == 0:
                    ans = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
