## Brute Force

class BruteForceSolution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        best = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                if len(set(sub)) == len(sub):
                    best = max(best, j - i)
        return best

## O(2N)
class BetterSolution(object):
    def lengthOfLongestSubstring(self, s):
        from collections import Counter
        chars = Counter()

        left = right = 0

        result = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1
            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            result = max(result, right - left + 1)

            right += 1
        return result

## O(N)
class OptimalSolution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        ans = 0
        # charToNextIndex stores the index after current character
        charToNextIndex = {}

        left = 0
        # try to extend the range [i, j]
        for right_plus_one in range(n):
            if s[right_plus_one] in charToNextIndex:

                left = max(charToNextIndex[s[right_plus_one]], left)

            ans = max(ans, right_plus_one - left + 1)
            charToNextIndex[s[right_plus_one]] = right_plus_one + 1

        return ans