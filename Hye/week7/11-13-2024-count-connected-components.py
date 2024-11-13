class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        1. Build adjacent node dictionary/graph adj[node] = v
        2. dfs through to see if it's connected visited[node] = True
        3. count nodes that are not yet connected (visited) -== # components
        """
        num_components = 0
        visited = set()
        graph = defaultdict(list)

        # Build adjacent graph
        for v, w in edges:
            graph[v].append(w)
            graph[w].append(v)
        
        # dfs to find connected nodes
        def dfs(node):
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        # Find non-connected components
        for node in range(n):
            if node not in visited:
                dfs(node)
                visited.add(node)
                num_components += 1
        
        return num_components
        
