'''
fruits = [0,1,2,2]
'''
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) < 3:
            return len(fruits)
        
        l = 0 
        res = 0 
        fr_map = {fruits[l]: 1}

        for r in range(1, len(fruits)):
            f_r = fruits[r] # 0 
            f_l = fruits[l] # 1
            
            fr_map[f_r] = fr_map.get(f_r, 0) + 1
            
            while len(fr_map) > 2:
                fr_map[fruits[l]] -= 1
                if fr_map[fruits[l]] == 0:
                    del fr_map[fruits[l]]
                l += 1
            res = max(res, r-l+1)
        
        return res