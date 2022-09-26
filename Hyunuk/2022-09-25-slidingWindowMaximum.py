class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        q = collections.deque()
        l, r = 0, 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()
            if (r + 1) >= k:
                ret.append(nums[q[0]])
                l += 1
            r += 1
        return ret
