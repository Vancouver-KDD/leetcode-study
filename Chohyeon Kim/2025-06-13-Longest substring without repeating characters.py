class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        alph_set = set()

        longest = 0
        l = 0

        # a b c a b c b b
        #       r
        #   l
        for r in range(len(s)):

            if s[r] not in alph_set:
                alph_set.add(s[r])

            else:
                while s[r] in alph_set:
                    alph_set.remove(s[l])
                    l += 1

            alph_set.add(s[r])

            longest = max(longest, r - l + 1)

        return longest
