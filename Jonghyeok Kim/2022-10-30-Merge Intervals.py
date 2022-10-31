
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=(lambda x: x[0]))
        res = [intervals[0]]
        for inter in intervals[1:]:
            if res[-1][1] >= inter[0]:
                res[-1][1] = max(res[-1][1], inter[1])
            else:
                res.append(inter)
        return res