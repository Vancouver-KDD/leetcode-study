class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if res[-1][1] > start:
                count += 1
                res[-1][1] = min(res[-1][1], end)
            else:
                res.append([start, end])
        return count