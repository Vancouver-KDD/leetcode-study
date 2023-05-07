class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {} #num:index

        for index, num in enumerate(nums):
            diff = target - num
            if diff in dict:
                return [index, dict[diff]]

            dict[num] = index

    # Time complexity:
    # Space complexity: