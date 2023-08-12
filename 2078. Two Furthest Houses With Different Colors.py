# Amazon Visa
# There are n houses evenly lined up on the street, and each house is beautifully painted. 
# You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

# Return the maximum distance between two houses with different colors.

# The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

# Example 1:

# Input: colors = [1,1,1,6,1,1,1]
# Output: 3
# Explanation: In the above image, color 1 is blue, and color 6 is red.
# The furthest two houses with different colors are house 0 and house 3.
# House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
# Note that houses 3 and 6 can also produce the optimal answer.

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        start = 0 
        end = len(colors) - 1

        while start <= end:
            if colors[start] != colors[0]:
                return abs(len(colors) - 1 - start)
            elif colors[end] != colors[len(colors) - 1]:
                return end
            elif colors[start] != colors[end]:
                return abs(end - start)
            start += 1
            end -= 1
