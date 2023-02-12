class Solution:
    def isValid(self, s: str) -> bool:

        d = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False

        return len(stack) == 0

        ## O(n) time complexity but not that much fast by leetcode system...

        # while len(s) > 0:
        #     l = len(s)
        #     s = s.replace('()','').replace('{}','').replace('[]','')
        #     if l==len(s): return False
        # return True

        ## O(n^2) time complexity but.... not bad...