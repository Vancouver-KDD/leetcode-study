class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(numbers, temp):
            if len(temp) == len(nums):
                result.append(temp[:])
                return
            for i in range(len(numbers)):
                temp.append(numbers[i])
                helper(numbers[:i] + numbers[i + 1:], temp)
                temp.pop()
        helper(nums, [])
        return result