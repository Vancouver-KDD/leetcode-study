class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in nums:
            ansLen = len(ans)

            for i in range(ansLen):
                ans.append(ans[i] + [num])

        return ans