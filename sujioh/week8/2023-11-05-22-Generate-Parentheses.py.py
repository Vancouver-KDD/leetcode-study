from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        stack = [('(', 1, 0)]
        ans = []
        while stack:
            cur_ans, n_open, n_close = stack.pop()
            if len(cur_ans) == 2 * n:
                ans.append(cur_ans)
                continue
            if n_open < n:
                stack.append((cur_ans + '(', n_open + 1, n_close))
            if n_close < n_open:
                stack.append((cur_ans + ')', n_open, n_close + 1))
        return ans


s = Solution()
s.generateParenthesis(3)
