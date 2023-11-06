from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        d = {0: 1}
        ans = 0

        for i in range(len(nums)):
            prefixSum = prefixSum + nums[i]

            # find a prefixSum in dictionary 
            if prefixSum - k in d:
                ans = ans + d[prefixSum-k]
            
            # add a prefixSum to dictionary 
            if prefixSum in d:
                d[prefixSum] = d[prefixSum] + 1
            else:
                d[prefixSum] = 1

        return ans


s = Solution()
print(s.subarraySum([1, 2, 3], 3))


'''
Summary:
Review needed. 

Complexity:
 - Time: O(n): n is the number of chars
 - Space: O(n): n is length of chars 
'''
