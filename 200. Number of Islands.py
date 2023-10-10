# Amazon Facebook Google
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def valid(row, col):
            return 0 <= row < w and 0 <= col < h and grid[row][col] == '1'

        def dfs(row, col):
            for dx, dy in drs:
                next_row, next_col = row + dx, col + dy
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    dfs(next_row, next_col)

        seen = set()
        ans = 0
        drs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        w = len(grid)
        h = len(grid[0])
        for row in range(w):
            for col in range(h):
                if grid[row][col] == '1' and (row, col) not in seen:
                    ans += 1
                    seen.add((row, col))
                    dfs(row, col)
        return ans
