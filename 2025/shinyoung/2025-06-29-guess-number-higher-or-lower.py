# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return 6

def guessNumber(n):
    def dfs(left, right):
        num = left + (right - left) // 2
        if guess(num) == -1:
            return dfs(left, num - 1)
        elif guess(num) == 1:
            return dfs(num + 1, right)
        else:
            return num
    return dfs(1, n)


print(guessNumber(10))
# print(guessNumber(1))
# print(guessNumber(2))
