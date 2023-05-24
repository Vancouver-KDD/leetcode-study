class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(0, n + 1):
            str_num = str(bin(i).replace("0b", ""))
            num = 0
            for x in str_num:
                if x == '1':
                    num += 1
            result.append(num)
        return result
