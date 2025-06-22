""" 213. House Robber II / Medium
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this 
place are arranged in a circle. That means the first house is the neighbor 
of the last one. Meanwhile, adjacent houses have a security system connected, 
and it will automatically contact the police if two adjacent houses were 
broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
 
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Consider 3 different cases:
        From [2, 7, 9, 3, 1]
        1) [2, 7, 9, 3]
        2) [7, 9, 3, 1]
        3) 2

        Ex) index = 2, num = 9
        From [2, 7, 9, 3, 1]
                    i
        pre_rob = 0
        max_rob = 0
        temp = max(max_rob, prev_rob + curr)
        calculate max_rob for the three cases:
            1) [2, 7, 9, 3]
            2) [7, 9, 3, 1]
            3) 2
        """
        def get_max(nums):
            prev_rob = max_rob = 0
            for num in nums:
                temp = max(max_rob, prev_rob + num)
                prev_rob = max_rob
                max_rob = temp
            return max_rob
        
        return max(get_max(nums[:-1]), get_max(nums[1:]), nums[0])

        # Time: 2N (max) * 2 (slice in get_max) = O(N)
        # Space: O(1) + 2 * slicing the list = O(N) = O(N)

