# 125. Valid Palindrome

>Problem link: https://leetcode.com/problems/valid-palindrome/  
>submission detail: https://leetcode.com/problems/valid-palindrome/submissions/843820900/

```py
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        alphabet_list = list(filter(str.isalnum, s))
        
        l, r = 0, len(alphabet_list) - 1
        '''
        1, 2, 3
        홀수인경우 하나의 인덱스에서 만나고, 다음번에 l과 r의 인덱스가 바뀌게 된다
        
        1, 2, 3, 4
        짝수인 경우 만나지 않고, l과 r의 인덱스가 바뀌게 된다
        '''
        
        while l <= r:
            if not alphabet_list[l] == alphabet_list[r]:
                return False
            l += 1
            r -= 1
        
        return True
```
