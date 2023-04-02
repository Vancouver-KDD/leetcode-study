"""
70. Climbing Stairs
"""

class Solution:
    def insert(
        self, intervals, newInterval
    ) :
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



def main():
    s = Solution()


if __name__ == "__main__":
    main()
