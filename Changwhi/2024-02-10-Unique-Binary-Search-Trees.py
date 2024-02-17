class Solution:
    def numTrees(self, n: int) -> int:
#         if n == 0:
#             return 1
#         res = 0
#         for node in range(1, n + 1):
#             res += self.numTrees(node - 1) * self.numTrees(n - node)

#         return res

        numTrees = [1] * (n + 1)
        
        for trees in range(2, n + 1):
            temp = 0
            for root in range(1, trees + 1):
                left = root - 1
                right = trees - root 
                temp += numTrees[left] * numTrees[right]
            numTrees[trees] = temp
        return numTrees[-1]