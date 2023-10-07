# Facebook Amazon Samsung
# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Example 1:

# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        ans = []
        while queue:
            len_queue = len(queue)
            mv = float('-inf')
            for _ in range(len_queue):
                node = queue.popleft()

                mv = max(mv, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(mv)
        return ans
