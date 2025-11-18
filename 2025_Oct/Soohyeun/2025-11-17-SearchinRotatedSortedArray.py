class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [4,5,6,7,0,1,2]
        #  |     |     |
        # left side
        #  1) left < mid: left <= targe <= mid -> just check left side only, otherwise check right side
        #  2) left > mid: left < target or target < mid -> target could be in left side
        # right side:
        #  1) mid < right: mid <= target <= right -> just check right side only, othersie check left side
        #  2) mid > right: mid < target or target < left -> target could be in right side
        # left < right -> end iteration

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:  # left side is sorted
                if nums[left] <= target < nums[mid]:  # target could be in left side
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
