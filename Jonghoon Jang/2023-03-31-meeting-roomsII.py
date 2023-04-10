"""
70. Climbing Stairs
"""

class Solution:
    def canAttendMeetings(self, intervals) -> bool:
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



def main():
    s = Solution()


if __name__ == "__main__":
    main()
