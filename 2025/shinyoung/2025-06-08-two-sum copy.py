class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosum = {}

        for index, num in enumerate(nums):
            if num not in twosum:
                twosum[num] = index

        for index, num in enumerate(nums):
            the_other = target - num
            if the_other in twosum and index != twosum[the_other]:
                return [index, twosum[the_other]]
