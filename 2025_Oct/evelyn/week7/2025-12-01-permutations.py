class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        visited = [False]*len(nums)

        self.backtrack(nums, ans, curr, visited)

        return ans
        
    def backtrack(self, nums, ans, curr, visited):
        if len(curr) == len(nums):
            ans.append(curr.copy())
            return

        for i in range(len(nums)):
            if visited[i]: continue

            curr.append(nums[i])
            visited[i] = True

            self.backtrack(nums, ans, curr, visited)

            visited[i] = False
            curr.pop()