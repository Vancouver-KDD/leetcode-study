def lengthOfLongestSubstring(self, s:str) -> int:
    max_substring = 0
    check_dup = set()
    l = 0
    count = 0
    for r in range(len(s)):
        while s[r] in check_dup:
            check_dup.remove(s[l])
            l += 1
            count -= 1
        check_dup.add(s[r])
        count += 1
        max_substring = max(max_substring, count)
    return max_substring