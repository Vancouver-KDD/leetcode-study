class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        #sort the intervals by the starting point
        intervals.sort(key = lambda i : i[0])
        
        res = []
        
        
        for start, end in intervals:
            
            if not res or res[-1][1] < start:
                res.append([start,end])
            else:
                res[-1][1] = max(end, res[-1][1])
        
        
        return res
        
            
        
        