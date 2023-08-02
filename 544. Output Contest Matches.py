# During the NBA playoffs, we always set the rather strong team to play with the rather weak team,
# like make the rank 1 team play with the rank nth team, which is a good strategy to make the contest more interesting.
#
# Given n teams, return their final contest matches in the form of a string.
#
# The n teams are labeled from 1 to n, which represents their initial rank
# (i.e., Rank 1 is the strongest team and Rank n is the weakest team).
#
# We will use parentheses '(', and ')' and commas ',' to represent the contest team pairing.
# We use the parentheses for pairing and the commas for partition. During the pairing process in each round,
# you always need to follow the strategy of making the rather strong one pair with the rather weak one.


class Solution:
    def findContestMatch(self, n: int) -> str:
        if n == 2:
            return f"(1,2)"

        res = list(range(1, n + 1))
        while len(res) > 2:
            start = 0
            end = len(res) - 1
            tmp = []
            while start < end:
                tmp.append(f"({res[start]},{res[end]})")
                start += 1
                end -= 1
            res = tmp
        return f"({','.join(res)})"
