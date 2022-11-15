class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {"2": "abc",
             "3": "def",
             "4": "ghi",
             "5": "jkl",
             "6": "mno",
             "7": "pqrs",
             "8": "tuv",
             "9": "wxyz",
             }
        ret = []
        stk = []
        if not digits:
            return []
        for ch in hm[digits[0]]:
            stk.append(([ch], 1))
        while stk:
            arr, i = stk.pop()
            if len(arr) == len(digits):
                ret.append(''.join(arr))
                continue
            for ch in hm[digits[i]]:
                arr.append(ch)
                stk.append((arr[:], i+1))
                arr.pop()
        return ret
