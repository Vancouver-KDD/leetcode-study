class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,1,2]
        #  |    |   |
        # -> min value is in the unsorted side
        # right side is nusortedcheck mid > mid + 1 -> yes: mid + 1 is min value, otherwise left = mid + 1
        # left side is unsorted, check mid < mid - 1 -> yes: mid is min value, otherwise check left side only right = mid -1
        # -> both side is sorted-> the most left element is min value

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                # left side is unsorted: min value is in left side
                right = mid

            elif nums[mid] > nums[right]:
                # right side is unsoted: min value is in right side
                left = mid + 1

            else:
                # both side are sorted.
                return nums[left]
