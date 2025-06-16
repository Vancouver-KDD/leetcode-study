def isPalindrome(s):
    s = list(s)
    s = [c for c in s if c.isalnum()]
    s = [c.lower() for c in s]
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
