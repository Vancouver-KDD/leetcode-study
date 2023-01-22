"""
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]


Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash = {}

        if k == len(nums):
            return nums

        for n in nums:
            try:
                hash[n] += 1
            except KeyError:
                hash[n] = 1

        sorted_map = sorted(hash.items(), key=lambda x: x[1], reverse=True)
        sorted_hash = dict(sorted_map)

        return list(sorted_hash.keys())[:k]


def main():
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(s.topKFrequent([1], 1))


if __name__ == "__main__":
    main()
