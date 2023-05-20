class Solution:
    def climb_stairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1 = 2
        n2 = 3

        for _ in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
    
solution = Solution()

for i in range(15):
    print(i,":", solution.climb_stairs(i))
