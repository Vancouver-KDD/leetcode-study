class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        sum = n
        sums = set()

        while sum != 1:
            if sum < 10:
                sum = sum ** 2
            elif sum < 100:
                first = sum % 10
                second = sum // 10
                sum = first ** 2 + second ** 2
            else:
                first = sum % 10
                sum -= first
                second = (sum / 10) % 10
                third = sum // 100
                sum = first ** 2 + second ** 2 + third ** 2
            if sum in sums:
                return False
            sums.add(sum)
            if sum == 1:
                return True
