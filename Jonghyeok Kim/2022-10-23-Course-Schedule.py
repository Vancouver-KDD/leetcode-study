class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        def dfs(crs, visited):
            if i in visited:
                return False
            if crs in visited:
                return False
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            preMap[crs] = []
            return True
        for crs in preMap:
            visited =set()
            if not dfs(crs, visited):
                return False
        return True
    