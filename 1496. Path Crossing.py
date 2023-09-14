# Amazon
# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. 
# You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 
# Example 1:

# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set(['0_0'])
        curr = [0, 0]
        for point in path:
            if point == 'N': 
                curr[0] += 1
            elif point == 'S': 
                curr[0] -= 1
            elif point == 'E': 
                curr[1] += 1
            else: 
                curr[1] -= 1
            if f'{curr[0]}_{curr[1]}' in seen:
                return True
            seen.add(f'{curr[0]}_{curr[1]}')
        return False
