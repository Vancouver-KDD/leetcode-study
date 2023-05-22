
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]: # 1
                return False
        return True

# 1. If the current meeting is after the start time of the next meeting, I won't be able to attend all the meetings.