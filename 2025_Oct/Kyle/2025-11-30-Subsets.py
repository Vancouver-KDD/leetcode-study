class Solution:
    def subsets(self, nums):
        self.output = []
        self.backtrack(0, [], nums)
        return self.output

    def backtrack(self, first, curr, nums):
        self.output.append(curr[:])
        for i in range(first, len(nums)):
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()

