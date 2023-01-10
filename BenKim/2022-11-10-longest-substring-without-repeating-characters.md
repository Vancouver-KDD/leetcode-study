# 3. Longest Substring Without Repeating Characters

> Problem link: https: https://leetcode.com/problems/longest-substring-without-repeating-characters/  
> submission detail: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/741627071/  

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window 활용
        # without repeating이기 때문에 set을 활용해 중복 방지
        charSet = set()
        l = result = 0

        for r in range(len(s)):
            # 중복이 있는 경우 left포인터 이동
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # 인덱스를 순회하며 char을 모으고, max length를 갱신한다
            # 중복되는 단어가 나오면, 중복이 해결될때까지 왼쪽의 char를 지워나간다
            charSet.add(s[r])

            # 0번째 인덱스도 길이는 1이기 때문에, 포인터 차이에 1을 더해준다
            result = max(result, r - l + 1)

        return result
```
## while, defaultdict 사용
```py
import collections

def len_of_the_longest_substring_wo_repeating_chars(s: str) -> int:
    hm = collections.defaultdict(int)
    l = 0
    r = 0
    ret = 0
    while r < len(s):
        hm[s[r]] += 1
        while hm[s[r]] > 1:
            hm[s[l]] -= 1
            l += 1
        ret = max(ret, r - l + 1)
        r += 1
    return ret
```