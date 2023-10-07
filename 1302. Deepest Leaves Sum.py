# Google Amazon Apple
# Given the root of a binary tree, return the sum of values of its deepest leaves.
 
# Example 1:

# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return root
        ans = 0
        queue = deque([root])
        while queue:
            row_length = len(queue)
            ans = 0
            for _ in range(row_length):
                node = queue.popleft()
                ans += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
