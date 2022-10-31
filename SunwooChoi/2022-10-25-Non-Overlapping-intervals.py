class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # if length of intervals is equal to 1, don't need to delete any intervals
        if len(intervals) == 1:
            return 0
        
        # ascending sort by last element in the inner list
        intervals.sort(key=lambda el: el[1])
        # the available minimum interval point without overlapping
        last = intervals[0][1]
        ans = 0
        
        for i in range(1, len(intervals)):
            # if start interval time is not range of last interval point,
            # we can set new last minimum interval point
            if intervals[i][0] >= last:
                last = intervals[i][1]
            # if it is with in the range of interval, drop the interval
            else:
                ans += 1
        
        return ans

