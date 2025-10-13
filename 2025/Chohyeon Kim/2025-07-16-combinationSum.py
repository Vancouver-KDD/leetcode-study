class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(start: int, sum_arr: int, arr):

            if sum_arr == target:
                print(sum_arr)
                print(arr)
                res.append(arr.copy())
                return

            if sum_arr > target:
                return

            for i in range(start, len(candidates)):

                num = candidates[i]

                sum_arr += num
                arr.append(num)
                dfs(i, sum_arr, arr)

                sum_arr -= num
                arr.pop()

        dfs(0, 0, [])

        return res
