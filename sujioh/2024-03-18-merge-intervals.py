from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        ans = []
        
        for interval in intervals:
            if not ans or interval[0] > ans[-1][1]:
                ans.append(interval)
            else:
                first = ans[-1][0]
                second = max(interval[1], ans[-1][1])
                ans.pop()
                ans.append([first, second]) 
        return ans
        