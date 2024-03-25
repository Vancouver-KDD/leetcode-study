from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        prev = None
        count = 0 

        for itv in intervals:
            if not prev or prev[1] <= itv[0]:
                count += 1
                prev = itv
        return len(intervals) - count

'''
이 문제를 풀기 위해서는 일단 서브어레이를 엔드 포인트를 사용해 어센딩으로 솔트해야함.
이유?
일찍 끝나는 인터벌을 살리면 겹치는 부분을 최소화할 수 있음.

overall procedure 
서브어레이를 엔드 포인트를 기준으로 어센딩으로 솔트: 
- 처음에는 각 서브어레이를 그것의 끝점을 기준으로 오름차순으로 정렬합니다. 
- 이는 더 일찍 끝나는 인터벌을 우선적으로 선택할 수 있도록 합니다. 이렇게 하면 겹치는 부분을 최소화할 수 있습니다.

인터벌이 이전 인터벌과 겹치는지 확인: 
- 정렬된 인터벌들을 순회하면서 각 인터벌이 이전 인터벌과 겹치는지 여부를 확인합니다. 
- 겹치는지 여부는 현재 인터벌의 시작점이 이전 인터벌의 끝점보다 작거나 같은지로 판단할 수 있습니다.

겹치지 않을 경우 처리: 
- 현재 인터벌이 이전 인터벌과 겹치지 않는 경우, 이전 인터벌을 현재 인터벌로 업데이트하고, 카운터를 하나 증가시킵니다. 
- 이는 겹치는 부분을 최소화하면서 비중첩된 인터벌의 수를 셀 수 있게 합니다.
 
'''
