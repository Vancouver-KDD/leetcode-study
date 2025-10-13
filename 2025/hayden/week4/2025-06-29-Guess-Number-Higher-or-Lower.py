# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        #set a range from 0 - n
        #mid of 0 - n
        #input mid to check() function
        #if check(mid) == -1 -> move the left side more to the right
        #if check(mid) == 1 -> move the right side more to the left
        #if check(mid) == 0 -> r eturn that number
        #otherwise, return -1

        left = 0
        right = n

        while left <= right:

            mid = (left + right) // 2

            if guess(mid) == -1:
                right = mid - 1
            elif guess(mid) == 1:
                left = mid + 1
            else :
                return mid

        return -1