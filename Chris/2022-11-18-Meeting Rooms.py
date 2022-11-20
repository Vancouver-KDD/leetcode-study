class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True
        intervals.sort(key=lambda x: x[0])
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start < prevEnd:
                return False    
            prevEnd = end
            
        return True
        
            
        