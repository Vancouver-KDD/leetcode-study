class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if ''.join(sorted(s)) == ''.join(sorted(t)):
            return True
        return False


s = Solution()
prev = str(input())
nxt = str(input())
print(s.isAnagram(prev, nxt))
