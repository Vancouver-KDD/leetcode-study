class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            
        
        #create preMap
        preMap = {}
        for crs in range(numCourses):
            preMap[crs] = []
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        #create visit list to check whether this algorithm visit the same vertex or not
        visit = set()
        
        #dfs
        def dfs(crs):
            # if crs is already in the visit list
            if crs in visit:
                return False
            
            # if crs doesn't have any prerequisites
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        # to handle the graph that is not tree(is not fully connected )
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
                
            