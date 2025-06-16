class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans = dict()

        for index, num in enumerate(nums):
            diff = target - num
            if diff in ans:
                return [index, ans[diff]]
            ans[num] = index

        #time complexity = O(n), n being length of nums
        #space complexity = O(n)