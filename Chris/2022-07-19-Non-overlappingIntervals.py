class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
                
        
        #sort the intervals by the starting point
        intervals.sort(key = lambda i : i[0])
        
        
        res = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            
            if prevEnd <= start:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end,prevEnd)
        
        
        return res