class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res
    
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
    
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prev_interval = intervals[0]
        res = 0
        for start, end in intervals[1:]:
            if start < prev_interval[1]:
                res += 1
                if end < prev_interval[1]:
                    prev_interval = [start,end]
            else:
                prev_interval = [start,end]
        return res
    
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i[0])

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] > i2[0]:
                return False
        return True
    
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time = []
        for start, end in intervals:
            time.append((start, 1))
            time.append((end, -1))
        
        time.sort(key=lambda x: (x[0], x[1]))
        
        count = 0
        max_count = 0
        for t in time:
            count += t[1]
            max_count = max(max_count, count)
        return max_count