def checkInclusion(self, s1: str, s2: str) -> bool:
    s2char = [0] * 26
    s1char = [0] * 26
    for s in s1:
        s1char[ord(s) - ord('a')] += 1
    
    left = 0
    right = 0
    while left < len(s2):
        while right < len(s2) and right - left < len(s1):
            s2char[ord(s2[right]) - ord('a')] += 1
            right += 1
        if s1char == s2char:
            return True
        s2char[ord(s2[left]) - ord('a')] -= 1
        left += 1
    return False