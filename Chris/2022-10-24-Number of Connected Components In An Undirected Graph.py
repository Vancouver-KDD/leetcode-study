class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Create an adjacent list
        adList = {}
        for i in range(n):
            adList[i] = []
            
        for n1, n2 in edges:
            adList[n1].append(n2)
            adList[n2].append(n1)
            
        def bfs(node):
            q = collections.deque()
            q.append(node)
            while q:
                cur = q.pop()
                visited.add(cur)
                for nbr in adList[cur]:
                    if nbr not in visited:
                        q.append(nbr)
                
        visited = set()
        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                bfs(node)
        
        return count