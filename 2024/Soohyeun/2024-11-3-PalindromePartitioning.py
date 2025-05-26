class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtracking(sub_s, index):
            if index >= len(s):
                res.append(sub_s[:])
                return
            right = index
            while right < len(s):
                if is_palindrome(index, right):
                    sub_s.append(s[index:right + 1])
                    backtracking(sub_s, right + 1)
                    sub_s.pop()
                right += 1

        backtracking([], 0)

        return res