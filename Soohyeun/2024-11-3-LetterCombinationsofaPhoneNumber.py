class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        num_letters = {2:["a","b","c"], 3:["d","e","f"], 4:["g","h","i"], 5:["j","k","l"], 6:["m","n","o"], 7:["p","q","r","s"], 8:["t","u","v"], 9:["w","x","y","z"]}
        digits_len = len(digits)
        res = []
        def back_tracking(s, index):
            nonlocal digits_len
            if index >= digits_len:
                res.append(s)
                return
            for letter in num_letters[int(digits[index])]:
                back_tracking(s + letter, index+1)

        back_tracking("", 0)

        return res