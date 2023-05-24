class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        n = str(bin(n))

        num = 0
        for i in n:
            if i is '1':
                num += 1
        return num
