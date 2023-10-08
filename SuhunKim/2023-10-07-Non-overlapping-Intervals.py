class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        res = 0
        lastInterval = intervals.pop(0)

        while intervals:
            currInterval = intervals.pop(0)
            if lastInterval[1] <= currInterval[0]:
                lastInterval = currInterval
            else:
                res += 1
                if lastInterval[1] >= currInterval[1]:
                    lastInterval = currInterval

        return res