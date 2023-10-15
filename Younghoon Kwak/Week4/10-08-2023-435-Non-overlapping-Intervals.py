class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        def dfs(idx):
            if idx==len(intervals):
                return 0

            take = 1+dfs(idx+1)

            left = idx+1
            right = len(intervals)-1
            while left<=right:
                mid = (left+right)//2
                if intervals[mid][0]<intervals[idx][1]:
                    left = mid+1
                else:
                    right = mid-1
            noTake = left-idx-1+dfs(left)
            return min(take, noTake)
        return dfs(0)