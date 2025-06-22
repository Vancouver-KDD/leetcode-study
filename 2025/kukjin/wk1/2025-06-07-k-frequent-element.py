class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums: 
            if n in dic: 
                dic[n] += 1
            else:
                dic[n] = 1

        # Sort by frequency (descending)
        sorted_items = sorted(dic.items(), key=lambda item: item[1], reverse=True)

        # Extract the top k keys
        return [item[0] for item in sorted_items[:k]]