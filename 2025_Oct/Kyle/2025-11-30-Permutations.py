class Solution(object):
    def permute(self, nums):
        output = []

        def backtrack(curr):
            if len(curr) == len(nums):
                output.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        backtrack([])

        return output