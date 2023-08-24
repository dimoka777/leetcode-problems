# Google
# Given a binary tree with the following rules:

# root.val == 0
# If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
# If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2

# Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

# Implement the FindElements class:

# FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
# bool find(int target) Returns true if the target value exists in the recovered binary tree.

# Example 1:

# Input
# ["FindElements","find","find"]
# [[[-1,null,-1]],[1],[2]]
# Output
# [null,false,true]
# Explanation
# FindElements findElements = new FindElements([-1,null,-1]); 
# findElements.find(1); // return False 
# findElements.find(2); // return True 


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.db = set()
        self.db.add(0)
        root.val = 0

        stack = [root]
        while stack:
            node = stack.pop()
            
            if node.left:
                node.left.val = 2 * node.val + 1
                self.db.add(node.left.val)
                stack.append(node.left)
            
            if node.right:
                node.right.val = 2 * node.val + 2
                self.db.add(node.right.val)
                stack.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.db
