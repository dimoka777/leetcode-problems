# Virtu Financial
# You have some apples and a basket that can carry up to 5000 units of weight.

# Given an integer array weight where weight[i] is the weight of the ith apple, return the maximum number of apples you can put in the basket.

 

# Example 1:

# Input: weight = [100,200,150,1000]
# Output: 4
# Explanation: All 4 apples can be carried by the basket since their sum of weights is 1450.


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        ans = cnt = 0
        weight.sort()
        for w in weight:
            ans += w
            if ans > 5000:
                break
            cnt += 1
        return cnt
                
