class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        set_nums = set(nums)

        for num in nums:
            if freq_dict.get(num, 0):
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        return nlargest(k, freq_dict.keys(), key=freq_dict.get)
