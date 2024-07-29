class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 1 2 3 4
        # 21 31 41 32 42
        # 312 412 341

        ans = []
        def backTracking(curr, first_num):
            if len(curr) == k:
                ans.append(curr[:])
                return

            for i in range(first_num, n+1):
                curr.append(i)
                backTracking(curr, i + 1)
                curr.pop()

        backTracking([], 1)
        return ans