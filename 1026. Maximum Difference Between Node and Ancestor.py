# Amazon Facebook Google
# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

# Example 1:

# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def max_diff(node, cur_max, cur_min):
            if not node:
                return cur_max - cur_min
            
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = max_diff(node.left, cur_max, cur_min)
            right = max_diff(node.right, cur_max, cur_min)
            return max(left, right)
            
        return max_diff(root, root.val, root.val)
