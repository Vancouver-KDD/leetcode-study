"""
70. Climbing Stairs
"""

class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort()
        # n - 1
        # n-2,  n-1,  n
        #       last
        for i in range(len(intervals) - 1):
            # intervals[i][1] end of i meeting
            # intervals[i+1][0] start of i+1 meeting
            if intervals[i][1] > intervals[i+1][0]:
                return False

        return True



def main():
    s = Solution()


if __name__ == "__main__":
    main()
