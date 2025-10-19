class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        count_map = defaultdict(list)
        res = []

        for num in nums: 
            count[num] = count.get(num, 0) + 1 

        for key in count: 
            counts = count[key]
            count_map[counts].append(key)
        

        for counts in range(len(nums), 0, -1):
            for val in count_map[counts]:
                if k == 0: 
                    return res 
                res.append(val)
                k-=1
        
        return res 



        