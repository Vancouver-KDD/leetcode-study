from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=(lambda x: x[0]))
        output = [intervals[0]]
        for start, end in intervals:
            if start <= output[-1][1]:
                output[-1][1] = max(end, output[-1][1])
            else:
                output.append([start,end])
        return output