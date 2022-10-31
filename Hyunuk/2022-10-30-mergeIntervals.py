class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def is_overlapped(a, b):
            return a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]
        
        def merge(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]
        
        ret = []
        intervals.sort(key=lambda x: x[0])
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if is_overlapped(curr, intervals[i]):
                curr = merge(curr, intervals[i])
            else:
                ret.append(curr)
                curr = intervals[i]
        ret.append(curr)
        return ret
