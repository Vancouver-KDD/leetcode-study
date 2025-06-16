def lengthOfLongestSubstring(s):
    left, right = 0, 0
    result = ""
    while left < len(s) and right <= len(s):
        print((s[left:right]))
        print(len(s[left:right]), len((set(s[left:right]))))
        if len(s[left:right]) == len(set(s[left:right])):
            if len(s[left:right]) > len(result):
                result = s[left:right]
                print("result", result)
            right += 1
        else:
            left += 1
    return len(result)


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring("cdd"))
print(lengthOfLongestSubstring("dvdf"))
