class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ret = prev = 0
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[prev][1] > intervals[i][0]:
                if intervals[prev][1] > intervals[i][1]:
                    prev = i
                ret += 1
            else:
                prev = i
        return ret
