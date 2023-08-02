# You are given a positive integer n.
#
# Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.
#
# Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.
#
# Return an integer array answer where answer = [even, odd].
from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        res = [0, 0]
        for i, v in enumerate(bin(n)[2:][::-1]):
            if v == '1':
                if i % 2 == 0:
                    res[0] += 1
                else:
                    res[1] += 1
        return res
