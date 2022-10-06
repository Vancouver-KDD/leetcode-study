# 338. Counting Bits

> problem link: https://leetcode.com/problems/counting-bits/  
> submission detail:  
> - https://leetcode.com/submissions/detail/814893306/  
> -  https://leetcode.com/submissions/detail/731749188/

```py
class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []
        for i in range(n+1):

            count = 0
            while i > 0:
                # 오른쪽 끝의 값을 확인하고
                count += i % 2

                # 한칸씩 오른쪽으로 옮긴다
                i = i // 2
            res.append(count)

        return res

```

```py
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0, n+1):
            result.append(bin(i).count('1'))
            
        return result
        
```
