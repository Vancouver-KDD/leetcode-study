class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def cycle(v, G, R, B):
            if v in R: 
                return True
            R.add(v)
            if v in G:
                for _v in G[v]:
                    if _v not in B and cycle(_v, G, R, B): 
                        return True
            R.remove(v)
            B.add(v)
            return False
        
        G = collections.defaultdict(list)
        R = set()
        B = set()
        for p in prerequisites:
            G[p[0]].append(p[1])
        for v in G:
            if v not in B and cycle(v, G, R, B): 
                return False
        return True