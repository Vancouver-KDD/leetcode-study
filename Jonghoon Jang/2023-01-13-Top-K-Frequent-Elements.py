"""
347. Top K Frequent Elements
Given an integer array nums and an integer k,
 return the k most frequent elements. You may return the answer in any order.
"""
import heapq


class Solution:
    # 1. hash table
    # Time complexity: O(N * K*logK) :
    # Space complexity: O(NK)
    def topKFrequent(self, nums, k):
        counter_dict = {}

        for num in nums:
            if num not in counter_dict:
                counter_dict[num] = 1
            else:
                counter_dict[num] += 1

        frequencies = sorted(counter_dict.values())  # O(N*logK) sort the list
        k_freq = frequencies[-k:]

        return [key for key, value in counter_dict.items() if value in k_freq]

    # 1. hash table
    # Time complexity: O(N * logK) :  insert and pop for heap
    # Space complexity: O(N + K): store the hash map
    def topKFrequentHeap(self, nums, k):
        counter_dict = {}

        for num in nums:
            if num not in counter_dict:
                counter_dict[num] = 1
            else:
                counter_dict[num] += 1

        max_heap = []
        for frequency in counter_dict.values():
            heapq.heappush(max_heap, -frequency)

        top_k_freq_elements = []
        for i in range(k):
            top_k_freq_elements.append(-heapq.heappop(max_heap))

        return [key for key, value in counter_dict.items() if value in top_k_freq_elements]


def main():
    s = Solution()

    print(s.topKFrequent([1,1,1,2,2,3], 2))
    print(s.topKFrequentHeap([1,1,1,2,2,3], 2))


if __name__ == "__main__":
    main()
