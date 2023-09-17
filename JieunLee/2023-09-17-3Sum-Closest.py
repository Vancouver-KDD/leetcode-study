# O(n^2) time | O(n) space where n is the length of the input array nums
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = target + 100000
        for i in range(len(nums) - 2) :
            left = i + 1
            right = len(nums) - 1

            while left < right :
                sum = nums[i] + nums[left] + nums[right]
                if abs(target - sum) < abs(target - closest_sum):
                    closest_sum = sum
                
                if target > sum:
                    left += 1
                elif target < sum:
                    right -= 1
                else:
                    return sum

        return closest_sum