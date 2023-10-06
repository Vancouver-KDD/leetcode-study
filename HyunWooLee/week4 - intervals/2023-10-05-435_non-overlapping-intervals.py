class Solution:
    '''
    runtime: O(n*lg(n))
    space: O(n)
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prev_end = intervals[0][1]

        result = 0
        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            if curr_start < prev_end:
                result += 1
                prev_end = min(prev_end, curr_end)
            else:
                prev_end = curr_end
        return result