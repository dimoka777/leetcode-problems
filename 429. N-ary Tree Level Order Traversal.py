# Amazon Adobe Google
# Given an n-ary tree, return the level order traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

# Example 1:

# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:
            lvl = []
            for i in range(len(queue)):
                node = queue.popleft()
                lvl.append(node.val)
                queue.extend(node.children)
            res.append(lvl)
        return res
