# Facebook Amazon Apple
# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# Example 1:

# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ans = [float('-inf'), float('inf')]
        lvl = 0
        while queue:
            lvl += 1
            lvl_sum = 0
            for i in range(len(queue)):
                node = queue.popleft()
                lvl_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            ans = max(ans, [lvl_sum, lvl], key=lambda x: x[0])
        return ans[1]
