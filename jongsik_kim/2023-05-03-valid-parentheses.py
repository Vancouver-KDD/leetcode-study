import queue


class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def isValid(self, s: str) -> bool:
        hashmap = {'(': ')', '{': '}', '[': ']'}
        char_stack = []
        if len(s) == 1:
            return False
        if len(s) < 1 or len(s) > 10**4:
            raise ValueError('Invalid Length')
        for i in s:
            if i in hashmap:
                char_stack.append(i)
            elif len(char_stack) == 0 or hashmap[char_stack.pop()] != i:
                return False
        return len(char_stack) == 0

        # TRY_2
        # Failure: "(){}}{"
        # hashmap = {')': '(', '}': '{', ']': '['}
        # char_stack = [s[0]]
        # for i in range(1, len(s)):
        #     if s[i] in hashmap:
        #         if char_stack.pop() == hashmap[s[i]]:
        #             continue
        #         else:
        #             return False
        #     else:
        #         char_stack.append(s[i])
        # return len(char_stack) == 0

        # TRY_1
        # Failure: "{[]}"
        # hashmap = {'(': ')', '{': '}', '[': ']'}
        # for i in range(len(s)):
        #     if s[i] in hashmap:
        #         if hashmap[s[i]] is not s[i + 1]:
        #             return False
        # return True


s = Solution()
print(s.isValid(str(input())))
