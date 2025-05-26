class Solution:
    def decodeString(self, s: str) -> str:
        digits = {"1","2","3","4","5","6","7","8","9","0"}
        res = ""
        i = 0
        repeat = ""
        repeat_stack = []
        word = ""
        word_stack = []
        for character in s:
            if character in digits:
                if repeat == "" and len(repeat_stack) != 0:
                    word_stack.append(word)
                    word = ""
                repeat += character
            elif character == "[":
                repeat_stack.append(int(repeat))
                repeat = ""
            elif character == "]":
                a = ""
                for _ in range(repeat_stack.pop()):
                    a += word
                if len(word_stack) == 0:
                    res += a
                    word = ""
                else:
                    word = word_stack.pop() + a
            else:
                if len(repeat_stack) == 0:
                    res += character
                else:
                    word += character
        return res