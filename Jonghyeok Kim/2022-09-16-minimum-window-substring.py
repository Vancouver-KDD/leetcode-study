class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window = {}
        countT = collections.Counter(t)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], len(s)+1
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != len(s)+1 else ""

# 1. find any match
# 2. move right pointer to find the next value of left pointer
# 3. if a char that is not the left pointer value in t is found while moving the right pointer, decrease t dict value
# 4. if the left pointer value is found, pop left until a char in t is found. If the value of the char in the t_dict is negative, keep poping
# 5. repeat until right pointer reach to the end
