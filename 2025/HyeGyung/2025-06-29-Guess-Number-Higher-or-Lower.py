# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n

        while True:
            mid = (left + right) // 2
            num = guess(mid)

            if num == -1 :
                right = mid -1
            elif num == 0:
                return mid
            else :
                left = mid + 1

