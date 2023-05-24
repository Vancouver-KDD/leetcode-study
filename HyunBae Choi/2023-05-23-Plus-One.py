# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Constraints:
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

# 1. loop from the back of the list, decrementing by 1
# 2. if the current digit + 1 equals 10, set the current digit to 0
# 3. else, add 1 to the digit and return the list
# 4. in the case the 1 carries over all the way to the front, append a 1 to the front of the list and return

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 == 10:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
                
        digits.insert(0, 1)
        return digits