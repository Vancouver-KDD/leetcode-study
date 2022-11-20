class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        res = r
        
        
        
        def is_possible_speed(k:int) -> bool:
            total = 0
            
            for p in piles:
                total += p // k
                if p % k != 0:
                    total += 1
                
            return total <= h
            
            
            
        # Find min possible speed between 1 and max(piles)
        while l <= r:
            m = (l+r) // 2
            
            if is_possible_speed(m):
                res = m
                r = m-1
            else:
                l = m+1
                
        return res
        
        
        
        