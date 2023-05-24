# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Constraints:
# 1 <= n <= 231 - 1

# 1.    create a hash set to keep track of visited numbers
# 2.    while the current sum of squares of n digits is not in the hash set, calculate the new sum of squares of n digits
# 2.5   the helper function will take n, and isolate a digit using modulus division by 10
#       then it will take the digit, square it, and add it to the total sum
#       update the value of n by doing a floor division of 10
# 3.    if n is currently 1, return True, else repeat
# 4.    if a number is revisited, there is a loop, meaning it will never reach 1, therefore, return False

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        
        return False
    
    def sumOfSquares(self, n):
        total_sum = 0

        while n:
            curr_digit = n % 10
            curr_digit_squared = curr_digit ** 2
            total_sum += curr_digit_squared
            n = n // 10

        return total_sum