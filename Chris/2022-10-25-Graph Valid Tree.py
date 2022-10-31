class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adList = {}
        for i in range(n):
            adList[i] = set()
        for n1, n2 in edges:
            adList[n1].add(n2)
            adList[n2].add(n1)
        visiting = set()
        
        def dfs(node: int) -> bool:
            if node in visiting:
                return False
            visiting.add(node)
            
            for nbr in adList[node]:
                adList[nbr].remove(node)
                if not dfs(nbr):
                    return False
            return True
            
        if not dfs(0):
            return False
        
        return len(visiting) == n
        