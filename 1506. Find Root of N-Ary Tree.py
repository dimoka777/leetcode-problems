# You are given all the nodes of an N-ary tree as an array of Node objects, where each node has a unique value.
#
# Return the root of the N-ary tree.
#
# Custom testing:
#
# An N-ary tree can be serialized as represented in its level order traversal
# where each group of children is separated by the null value (see examples).

# The testing will be done in the following way:
#
# 	The input data should be provided as a serialization of the tree.
# 	The driver code will construct the tree from the serialized input data and
# 	put each Node object into an array in an arbitrary order.
# 	The driver code will pass the array to findRoot, and
# 	your function should find and return the root Node object in the array.
# 	The driver code will take the returned Node object and serialize it.
# 	If the serialized value and the input data are the same, the test passes.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        tmp = 0
        for node in tree:
            tmp += node.val
            for child in node.children:
                tmp -= child.val

        for node in tree:
            if node.val == tmp:
                return node
