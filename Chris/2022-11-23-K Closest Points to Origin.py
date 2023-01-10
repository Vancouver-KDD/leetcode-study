class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        index_dists = []
        for i, coord in enumerate(points):
            distance = (coord[0]**2 + coord[1]**2) ** (1/2)
            index_dists.append((i,distance))
            
        index_dists.sort(key=lambda x:x[1], reverse=False)
        
        res = []
        
        for i in range(k):
            res.append(points[index_dists[i][0]])
            
        return res
        
        