import collections
from typing import List

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        r = 0 
        output = []
        q = collections.deque()

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if q[0] < l:
                q.popleft()
                
            if r+1 >= k:
                output.append(nums[q[0]])
                l += 1

        return output
            