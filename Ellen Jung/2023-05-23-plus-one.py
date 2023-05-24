class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 0
        digit = 0
        for i in range(len(digits) - 1, -1, -1):
            sum += digits[digit] * 10 ** i
            digit += 1
        sum += 1

        result = []
        has_zero = False
        if sum % 10 == 0:
            has_zero = True
        while sum != 0:
            num = sum // (10 ** (len(str(sum)) - 1))
            result.append(num)
            sum -= num * (10 ** (len(str(sum)) - 1))
        if has_zero:
            result.append(0)
        return result
