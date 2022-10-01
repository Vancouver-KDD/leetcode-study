class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # ascending sort in place
        nums.sort()

        for idx in range(len(nums)-2):
            # skip current index if it is same value with the previous one
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            left, right = idx + 1, len(nums) -1
            while left < right:
                cur_sum = nums[left] + nums[right] + nums[idx]
                if cur_sum < 0:
                    left += 1 # increase sum
                elif cur_sum > 0:
                    right -= 1 # decrease sum
                else:
                    ans.append([nums[left], nums[right], nums[idx]])
                    # skip the same values
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans