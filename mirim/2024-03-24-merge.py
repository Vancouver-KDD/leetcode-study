# https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        rs = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = rs[-1][1]
            if start <= lastEnd:
                rs[-1][1] = max(lastEnd, end)
            else:
                rs.append([start, end])
        return rs
