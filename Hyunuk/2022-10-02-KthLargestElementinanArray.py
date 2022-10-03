class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def select(l, h):
            pivot = partition(l, h)
            if k < pivot:
                return select(l, pivot - 1)
            if k > pivot:
                return select(pivot + 1, h)
            return nums[k]
        
        def partition(l, h):
            p_idx = random.randint(l, h)
            pivot = nums[p_idx]
            nums[p_idx], nums[h] = nums[h], nums[p_idx
                                                ]
            store_idx = l
            for i in range(l, h):
                if nums[i] < pivot:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1
            
            nums[store_idx], nums[h] = nums[h], nums[store_idx]
            return store_idx
        k = len(nums) - k
        return select(0, len(nums) - 1)
    
"""
[1324765]
    p
       h
p=3
"""
