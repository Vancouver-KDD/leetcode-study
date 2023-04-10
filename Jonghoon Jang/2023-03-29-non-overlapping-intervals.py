"""
70. Climbing Stairs
"""

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda interval: interval[1])
        end = float('-inf')
        count = 0
        for interval in intervals:
            if interval[0] >= end:
                end = interval[1]
            else:
                count += 1
        return count



def main():
    s = Solution()


if __name__ == "__main__":
    main()
