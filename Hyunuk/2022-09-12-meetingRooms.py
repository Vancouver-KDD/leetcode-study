class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        def is_overlapped(a, b):
            return a[0] <= b[0] < a[1] or a[0] < b[1] <= a[1]
        
        if not intervals:
            return True
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        
        for i in range(1, len(intervals)):
            if is_overlapped(prev, intervals[i]):
                return False
            prev = intervals[i]
        return True
