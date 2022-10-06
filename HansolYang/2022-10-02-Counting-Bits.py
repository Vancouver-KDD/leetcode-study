class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = [0]
        index = 0
        
        while n // (2**index) > 1:
            for i in range(2**index):
                ans.append(ans[i] + 1)
            index += 1
        
        index = 2**index
        s = 0
        
        while index <= n:
            ans.append(ans[s] + 1)
            s += 1
            index += 1
        
        return ans
                    
        
        