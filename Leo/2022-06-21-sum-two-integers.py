class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(math.log2(pow(2,a) * pow(2,b)))