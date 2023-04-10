class Solution:
    def can_attend_meetings(self, intervals):
        intervals.sort()
        prevEnd = intervals[-1][1]
        for start, end in intervals:
            if start > prevEnd:
                return False
        return True