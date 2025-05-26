from typing import List

#       d               e               f
#   g   h   i       g   h   i       g   h   i

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        number_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(index, curStr):
            if len(curStr) == len(digits):
                result.append(curStr)
                return
            for c in number_map[digits[index]]:
                backtrack(index + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return result

solution = Solution()
output = solution.letterCombinations("34")
print(output)
