class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < 1 or len(t) < 1 or len(s) > 5*(10**4) or len(t) > 5*(10**4):
            raise ValueError('Invalid Length')
        if ''.join(sorted(s)) == ''.join(sorted(t)):
            # compare two string strs after sorting
            return True
        return False


s = Solution()
prev = str(input())
nxt = str(input())
print(s.isAnagram(prev, nxt))
