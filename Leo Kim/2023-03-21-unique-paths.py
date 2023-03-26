class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        fact = [1] * (m + n)

        for i in range(2, m + n):
            fact[i] = fact[i - 1] * i

        return fact[m + n - 2] // (fact[m - 1] * fact[n - 1])