class Solution:
    # time complexity: O(log(n))
    # space complexity: O(1)
    def search(self, nums: list[int], target: int) -> int:
        if target not in nums:
            return -1
        left_index, right_index = 0, len(nums) - 1  # set indexes
        while left_index < right_index:
            mid = (left_index + right_index) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left_index = mid + 1
            elif target < nums[mid]:
                right_index = mid
        return left_index if nums[left_index] == target else -1

        # TRY_1
        # Failure: the nums list index changes
        # mid = len(nums) // 2
        # if nums[mid] == target:
        #     return mid
        # elif nums[mid] > target:
        #     print(nums[0:mid])
        #     return self.search(nums[0:mid], target)
        # elif nums[mid] < target:
        #     print(nums[mid:])
        #     return self.search(nums[mid:], target)


s = Solution()
nums1 = [-1, 0, 3, 5, 9, 12]
print(s.search(nums1, int(input())))
