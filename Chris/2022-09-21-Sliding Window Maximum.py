class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = collections.deque()
        l = r = 0
        res = []
        
        while r < len(nums):
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
        
            if r - l + 1 == k:
                res.append(nums[q[0]])
                if q[0] == l:
                    q.popleft()
                l += 1
            
            r += 1
            
        return res
            
        