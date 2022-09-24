class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if intervals == None or len(intervals) <= 1:
            return intervals
        
        intervals.sort()
        
        start = intervals[0][0]
        end = intervals[0][1]
        index = 1
        
        while index < len(intervals):
            i = intervals[index]
            if i[0] < end and i[1] > end:
                intervals[index-1][1] = i[1]
                end = i[1]
                intervals.remove(i)
            elif i[0] < end and i[1] <= end:
                intervals.remove(i)
            elif i[0] == end:
                intervals[index-1][1] = i[1]
                end = i[1]
                intervals.remove(i)
            else:
                start = i[0]
                end = i[1]
                index += 1
        
        return intervals