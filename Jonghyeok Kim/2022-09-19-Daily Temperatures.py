class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for idx, n in enumerate(temperatures):
            while stack and stack[-1][1] < n:
                tmp_idx, tmp_num = stack.pop()
                res[tmp_idx] = idx - tmp_idx
            stack.append((idx, n))
        return res