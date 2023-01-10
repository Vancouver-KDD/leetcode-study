# 435. Non-overlapping Intervals

> Problem link: https://leetcode.com/problems/non-overlapping-intervals/  
> submission detail: https://leetcode.com/submissions/detail/833365533/

```py
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 시작점을 기준으로 정렬
        intervals.sort()
        endPoint = intervals[0][1]
        result = 0
        # 1. 엔드포인트가 겹치지 않는경우
        # 엔드포인트는 현재 iterable의 엔드포인트로 이동, 0개노드 삭제
        # 2. 현재 스타트 포인트가 이전의 구간에 겹치고, 엔드포인트가 더 긴경우
        # 짧은 엔드포인트를 유지, 1개노드 삭제
        # 3. 현재 스타트 포이늩가 이전의 구간에 겹치고, 엔드포인트가 더 짧은경우
        # 짧은 엔드포인트를 유지 1개노드 삭제
        for start, end in intervals[1:]:
            if start >= endPoint:
                endPoint = end
            else:
                endPoint = min(endPoint, end)
                result += 1
        return result
        
```