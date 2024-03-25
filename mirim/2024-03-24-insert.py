# https://leetcode.com/problems/insert-interval/submissions/1213080770/
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda i: i[0])
        rs = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = rs[-1][1]
            if start <= lastEnd:
                rs[-1][1] = max(lastEnd, end)
            else:
                rs.append([start, end])
        return rs
