from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output_list = []

        def dfs(i, cur):
            if i == len(s):
                output_list.append(cur.copy())
                return

            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    cur.append(s[i:j+1])
                    dfs(j + 1, cur)
                    cur.pop()

        dfs(0, [])
        return output_list

    def isPali(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

solution = Solution()
output = solution.partition("aab")
print(output)
