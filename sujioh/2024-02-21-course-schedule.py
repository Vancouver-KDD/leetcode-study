class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {c: [] for c in range(numCourses)}
        
        for c, p in prerequisites:
            preMap[c].append(p)

        res = []
        visiting, verified = set(), set()

        def dfs(c):
            if c in visiting: 
                return False
            if c in verified:
                return True
            
            visiting.add(c)
            for p in preMap[c]:
                if dfs(p) == False:
                    return False
            visiting.remove(c)
            verified.add(c)
            res.append(c)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return False
        return True
            