class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 1  
        intervals.sort(key=lambda x: x[1])
        compare = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= compare:
                count += 1
                compare = intervals[i][1]
        if len(intervals) == 0:
            return 0

        return len(intervals) - count