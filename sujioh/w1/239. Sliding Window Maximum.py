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
            
'''
Note:

1. Intro 
The description is in the link, and the examples are:
https://leetcode.com/problems/sliding-window-maximum/description/

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
 
2.  Explanation:
a. For loop structure 
    1) Make a for loop, and it is for right pointer. 
    2) Left pointer on the other hand, will increase only after the len(sliding_window) is bigger than K

b. Inside for loop logics
- There are a few logics we have inside of the for loop 
    1) We will use queue, the queue will be strictly "decrementing" order. 
    Therefore, the q[0] will be the maximum value which we will append to output. 

    2) We will remove smaller values than current R, with WHILE loop.
    So that, all smaller values than R to be removed. 
    
    3) To update the window, we will remove if the queue has index smaller than L.


3. Key take-away 
    a. strictly decrementing queue
'''