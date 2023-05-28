class Solution:
    def getSquareSum(self, n: int):
        sum = 0
        for digit in str(n):
            sum += int(digit)**2
        return sum

    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = self.getSquareSum(n)
        return n == 1