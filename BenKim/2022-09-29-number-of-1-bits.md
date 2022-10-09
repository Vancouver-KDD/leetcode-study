# 191. Number of 1 Bits

> Problem link: https://leetcode.com/problems/number-of-1-bits/  
> [Python]submission detail: 
> https://leetcode.com/submissions/detail/814862792/  
> https://leetcode.com/submissions/detail/731711968/  
# 1
```py
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # 32번 반복됨
        while n > 0:
            
            # 오늘쪽 끝자리가 1인지 확인
            # 1과 AND하는 방법도 있다
            res += n % 2
            
            # 오른쪽 끝자리 이동
            # 2로 나누는 방법도 있다            
            n = n >> 1
        return res
```

# 2
```py
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
```