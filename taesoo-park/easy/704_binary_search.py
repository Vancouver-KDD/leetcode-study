class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        half = int(size/2)
        if target == nums[half]:
            return half
        elif target < nums[half]:
            return self.search(nums[:half], target)
        else:
            index = self.search(nums[half:], target)
            return index + half if index != -1 else -1