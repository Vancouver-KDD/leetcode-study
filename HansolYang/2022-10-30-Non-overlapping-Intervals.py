class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if intervals == None or len(intervals) <= 1:
            return 0
        
        intervals.sort()
        
        start = intervals[0][0]
        end = intervals[0][1]
        count = 0
        
        for i in intervals[1:]:
            
            if i[1] <= end or i[0] < end:
                count += 1
                
                if i[0] > start:
                    start = i[0]
                if end > i[1]:
                    end = i[1]
                
            else:
                start = i[0]
                end = i[1]
            
        return count