# AmazonDE ShawYou are given two 0-indexed integer arrays player1 and player2,
# that represent the number of pins that player 1 and player 2 hit in a bowling game, respectively.
#
# The bowling game consists of n turns, and the number of pins in each turn is exactly 10.
#
# Assume a player hit xi pins in the ith turn. The value of the ith turn for the player is:
# 	2xi if the player hit 10 pins in any of the previous two turns.
# 	Otherwise, It is xi.
#
#
# The score of the player is the sum of the values of their n turns.
#
# Return
# 	1 if the score of player 1 is more than the score of player 2,
# 	2 if the score of player 2 is more than the score of player 1, and
# 	0 in case of a draw.
#
# Example 1:
#
# Input: player1 = [4,10,7,9], player2 = [6,5,2,3]
# Output: 1
# Explanation: The score of player1 is 4 + 10 + 2*7 + 2*9 = 46.
# The score of player2 is 6 + 5 + 2 + 3 = 16.
# Score of player1 is more than the score of player2, so, player1 is the winner, and the answer is 1.
from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def cnt_points(lst):
            res = cnt = 0
            for i in lst:
                res += i
                if cnt > 0:
                    res += i
                    cnt -= 1

                if i == 10:
                    cnt = 2
            return res

        if cnt_points(player1) > cnt_points(player2):
            return 1
        elif cnt_points(player1) < cnt_points(player2):
            return 2
        else:
            return 0