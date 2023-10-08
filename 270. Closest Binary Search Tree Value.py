# Facebook Amazon Coupang
# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
# If there are multiple answers, print the smallest.

# Example 1:

# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return root
        
        res = root.val
        stack = [root]
        while stack:
            node = stack.pop()

            if (abs(target - node.val) < abs(target - res) or (abs(target - node.val) == abs(target - res) and node.val < res)):
                res = node.val

            if node.left and node.val > target:
                stack.append(node.left)
            
            if node.right and node.val < target:
                stack.append(node.right)

        return int(res)


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = root.val
        while root:
            ans = min(root.val, ans, key=lambda x: (abs(target - x), x))
            root = root.left if root.val > target else root.right
        return ans
