class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        output = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == target:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        return output


