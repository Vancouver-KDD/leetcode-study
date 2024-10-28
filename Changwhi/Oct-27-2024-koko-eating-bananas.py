class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles = [3, 6, 7, 11]
        
        posible time = [1 to 11]
        
        go throught 1 to 11 to see if KoKo can finish Bananas in time. 
        
        brute force O(max(piles) * piles)
        
        you can use binary search which is O(log(max(piles)*piles))
        
        1. make two pointer, 1 and max(p) <- we should loop through list of estimated time not the piles.
        2. loop through while left <= right
        3. find middle 
        4. perform calculate on piles with number of middel, ex, middle is 5 then, 3 / 6 -> 0.5 , round up, so 1.
        5. check the sum of results to see if it is equal or close to h. 
        6. keep looping through until right pointer passes by left
        
        """
        
        left, right = 1, max(piles)
        
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
            
            if time <= h:
                result = mid
                right = mid -1
            else: 
                left = mid + 1
        return result
        
            
            