# 242. Valid Anagram

>Problem link: https://leetcode.com/problems/valid-anagram/  
>[**Python**]submission detail: 
>- https://leetcode.com/submissions/detail/738851587/   
>- https://leetcode.com/problems/valid-anagram/submissions/842998234/

# dict 사용
```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letterDict = collections.defaultdict(int)

        s_arr = list(s)
        t_arr = list(t)

        for letter in s_arr:
            letterDict[letter] += 1

        for letter in t_arr:
            if letterDict[letter] == 1:
                del letterDict[letter]
            else:
                letterDict[letter] -= 1

        return True if letterDict == {} else False
```

# sorted 사용
```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))
```