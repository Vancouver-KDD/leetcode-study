class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for idx, n in enumerate(nums):
            tmp = two
            two = max(one+n, tmp)
            one = tmp
        return two
    
class Solution:
    def rob(self, nums: List[int]) -> int:                
        def inner_rob(nums):
            one, two = 0, 0
            for n in nums:
                tmp = two
                two = max(one+n, tmp)
                one = tmp
            return two
        return max(inner_rob(nums[1:]), inner_rob(nums[:-1])) if len(nums) != 1 else nums[0]
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        res, max_len = s[0], 1
        for i in range(1, len(s)):
            left, right = i-1, i
            while left > -1 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    res = s[left:right+1]
                    max_len = right - left + 1
                left -= 1
                right += 1

        if len(s) == 2:
            return res
        
        for i in range(1, len(s)-1):
            left, right = i-1, i+1
            while left > -1 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    res = s[left:right+1]
                    max_len = right - left + 1
                left -= 1
                right += 1
        return res
    
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        for i in range(1, len(s)):
            left, right = i-1, i
            while left > -1 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        for i in range(1, len(s)-1):
            left, right = i-1,i+1
            while left > -1 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res

class Solution:
    def numDecodings(self, s: str) -> int:
        res = [0] * (len(s)+1)
        res[len(s)] = 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                res[i] = 0
            else:
                res[i] = res[i+1]
            if (s[i] != "0" and i+1 < len(s) and int(s[i:i+2]) > 0 and int(s[i:i+2]) < 27):
                res[i] += res[i+2]
        return res[0]
