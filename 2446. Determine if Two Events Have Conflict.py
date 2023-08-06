# GoogleGoldman SachsYou are given two arrays of strings that represent two inclusive events
# that happened on the same day, event1 and event2,
# where:
# 	event1 = [startTime1, endTime1] and
# 	event2 = [startTime2, endTime2].
#
#
# Event times are valid 24 hours format in the form of HH:MM.
#
# A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).
#
# Return true if there is a conflict between two events. Otherwise, return false.
#
# Example 1:
#
# Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
# Output: true
# Explanation: The two events intersect at time 2:00.
from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return event1[0] <= event2[0] <= event1[1] or event2[0] <= event1[0] <= event2[1]