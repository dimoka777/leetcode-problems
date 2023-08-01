"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from typing import List


class Solution:
    def __init__(self):
        self.res = 0
        self.tmp = None

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if not employees:
            return employees

        self.tmp = {i.id: i for i in employees}
        stack = [id]
        while stack:
            node = self.tmp.get(stack.pop())
            self.res += node.importance
            if node.subordinates:
                stack.extend(node.subordinates)

        return self.res
