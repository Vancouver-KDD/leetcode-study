class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        memo = [0] * (len(s) + 1)
        memo[0], memo[1] = 1, 1

        for i in range(2, len(s) + 1):
            if s[i-1] == "0" and s[i-2] != "1" and s[i-2] != "2":
                return 0
            single_digit = memo[i-1] if s[i-1] != "0" else 0
            double_digit = memo[i-2] if 10 <= int(s[i-2:i]) <= 26 else 0

            memo[i] = single_digit + double_digit

        return memo[-1]