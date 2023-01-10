class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def is_overlapped(arr1, arr2):
            return arr1[0] <= arr2[0] <= arr1[1] or arr1[0] <= arr2[1] <= arr1[1]
        def merge(arr1, arr2):
            return [min(arr1[0], arr2[0]), max(arr1[1], arr2[1])]
        
        # put newinterval to intervals
        # sort by start time
        # iterate intervals while contiguous two are not overlapped
        # merge intervals while two are overlapped
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        i = 0
        ret = []
        while i < len(intervals) - 1 and not is_overlapped(intervals[i], intervals[i+1]):
            ret.append(intervals[i])
            i += 1
        merged = intervals[i]
        while i < len(intervals) - 1 and is_overlapped(merged, intervals[i+1]):
            merged = merge(merged, intervals[i+1])
            # print(merged, i, intervals)
            i += 1
        ret.append(merged)
        i += 1
        while i < len(intervals):
            ret.append(intervals[i])
            i += 1
        return ret
