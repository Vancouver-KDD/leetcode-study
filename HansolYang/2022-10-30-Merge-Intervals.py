class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = []
        
        for i in intervals:
            if i == intervals[0]:
                curr = i
            elif curr[1] >= i[0]:
                curr = [curr[0], max(i[1], curr[1])]
            else:
                res.append(curr)
                curr = i
                
        res.append(curr)
        
        return res