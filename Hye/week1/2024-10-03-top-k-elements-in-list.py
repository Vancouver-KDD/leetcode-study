""" Top K Elements in List
Given an integer array nums and an integer k,
return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

python hye/2024-10-03-top-k-elements-in-list.py
"""

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums).most_common(k)
        return sorted([c[0] for c in counter])


def main():
    s = Solution()

    # Example 1:
    print("\n Example1 \n")
    nums = [1,2,2,3,3,3]
    k = 2
    expected_output = [2,3]
    ans = s.topKFrequent(nums, k)
    print("expected_output: ", expected_output)
    print("ans: ", ans)
    assert expected_output == ans

    # Example 2:
    print("\n Example2 \n")
    nums = [7,7]
    k = 1
    expected_output = [7]
    ans = s.topKFrequent(nums, k)
    print("expected_output: ", expected_output)
    print("ans: ", ans)
    assert expected_output == ans

    # Test failure from submission
    print("\n Example3 \n")
    nums = [1,1,1,2,2,3]
    k = 2
    expected_output = [1, 2]
    ans = s.topKFrequent(nums, k)
    print("expected_output: ", expected_output)
    print("ans: ", ans)
    assert expected_output == ans

    print("Success!")
    
if __name__ == "__main__":
    main()
