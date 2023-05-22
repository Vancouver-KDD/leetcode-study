# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# from typing import (
#     List,
# )
# from lintcode import (
#     Interval,
# )

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

# 1. sort the intervals by ascending starting times (earliest starting to latest)
# 2. loop for the length of the intervals, starting at the 1st index (we want the ending time of the first, and the starting time of the second)
# 3. if the ending time of the first interval is greater than the starting time of the second interval, return False
# 4. if loop completes without returning False, all meetings can be attended, therefore, return True

class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)

        for i in range(1, len(intervals)): # start with index 1 and compare to the previous index
            first_interval = intervals[i - 1]
            second_interval = intervals[i]

            if first_interval.end > second_interval.start:
                return False
        
        return True

