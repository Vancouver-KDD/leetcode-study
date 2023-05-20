# https://www.lintcode.com/problem/920/
# https://peterdrinker.tistory.com/495

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def can_attend_meetings(self, intervals: list[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)

        for i in range(1, len(intervals)):
            temp1 = intervals[i - 1]
            temp2 = intervals[i]

            if temp1.end > temp2.start:
                return False
        return True
    
interval1 = Interval(0, 30)
interval2 = Interval(5, 10)
interval3 = Interval(15, 20)

interval4 = Interval(5, 8)
interval5 = Interval(9, 15)

intervals1 = []
intervals1.append(interval1)
intervals1.append(interval2)
intervals1.append(interval3)

intervals2 = []
intervals2.append(interval4)
intervals2.append(interval5)

solution = Solution()
print(solution.can_attend_meetings(intervals1))
print(solution.can_attend_meetings(intervals2))

