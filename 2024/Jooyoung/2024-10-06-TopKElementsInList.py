from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        mc = c.most_common(k)

        answer = []
        for n, _ in mc:
            answer.append(n)

        return answer


solution = Solution()
result = solution.topKFrequent([1,2,2,3,3,3,4,4,4,4,4,4,4,5,5,5,5], 2)
print(result)
