from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        ans = [] 
        1. identify the insert point and insert
            ans[-1][0] < newInterval[0] < curr[0]
        
        2. go over array again and merge if necessary 
        '''

        if len(intervals) == 0:
            return [newInterval]
        
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                intervals.insert(i-1, newInterval)
            if i == len(intervals)-1:
                intervals.insert(i-1, newInterval)
        
        intervals.sort(key=lambda x:x[0])
        

        ans = [] 
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                first = ans[-1][0]
                second = max(interval[1], ans[-1][1])
                ans.pop()
                ans.append([first, second])
        return ans 
