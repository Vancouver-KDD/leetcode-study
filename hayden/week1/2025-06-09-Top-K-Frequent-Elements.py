from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #counting the frequencies
        frequency = Counter(nums)

        #getting the top k most common using most_common method
        common = frequency.most_common(k)

        #creating a list to store only the keys
        answer = [key for key,_ in common]

        return answer
        