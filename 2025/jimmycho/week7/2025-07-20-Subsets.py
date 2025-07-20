class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(elements, temp):
            result.append(temp[:])
            for i in range(len(elements)):
                temp.append(elements[i])
                helper(elements[i+1:], temp)
                temp.pop()
        helper(nums, [])
        return result