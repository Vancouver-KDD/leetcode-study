class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #  u,l ...  r
        #  ..
        #  
        #  d
        l, r = 0, len(matrix[0])-1
        u, d = 0, len(matrix)-1
        res = []
        
        
        while(l <= r and u <= d):
            for i in range(l,r+1):
                res.append(matrix[u][i])
            u += 1
            for i in range(u,d+1):
                res.append(matrix[i][r])
            r -= 1
            
            # Check loop condition in the middle casue we just decreaseed the size of the rectangluar by one
            if (l > r or u > d):
                break
                
            for i in range(r,l-1,-1):
                res.append(matrix[d][i])
            d -= 1    
            for i in range(d,u-1,-1):
                res.append(matrix[i][l])
            l += 1
        
        return res
                