class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        ret = 0
        s_i, e_i = 0, 0
        while s_i < len(start):
            if start[s_i] >= end[e_i]:
                ret -= 1
                e_i += 1
            ret += 1
            s_i += 1
        return ret
