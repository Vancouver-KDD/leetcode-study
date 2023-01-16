class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while (left <= right):
            middle = left + ((right - left) // 2)
            if nums[middle] == target:
                return middle
            if nums[left] <= nums[middle]:
                # left is sorted and target is in left -> check left
                if target >= nums[left] and target <= nums[middle]:
                    right = middle - 1
                # left is sorted and target is not in left -> check right
                else:
                    left = middle + 1
            else:
                # left is not sorted -> right is sorted and target is in right -> check right
                if target >= nums[middle] and target <= nums[right]:
                    left = middle + 1
                # left is not sorted -> right is sorted and target is not in right -> check left
                else:
                    right = middle - 1
        return -1








