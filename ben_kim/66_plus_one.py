class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = ""
        
        for num in digits:
            str_digits += str(num)

        plus_one = str(int(str_digits) + 1)

        return [int(char) for char in plus_one]