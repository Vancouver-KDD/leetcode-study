# 56. Merge Intervals

> Problem link: https://leetcode.com/problems/merge-intervals/  
> submission detail: https://leetcode.com/submissions/detail/831149941/  

```py
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
                
        # 직전 인터벌 사이에 시작포인트가 들어가는지 확인하기 위해 정렬
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = result[-1][1]
            if lastEnd >= start:
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])

        return result
        
```