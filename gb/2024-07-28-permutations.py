class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subList = []
        visited = set()

        def backtrack(subList, visited):
            if len(subList) == len(nums):
                res.append(subList[:])
                return

            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                subList.append(nums[i])
                backtrack(subList, visited)
                subList.pop()
                visited.remove(i)

        backtrack(subList, visited)
        return res
