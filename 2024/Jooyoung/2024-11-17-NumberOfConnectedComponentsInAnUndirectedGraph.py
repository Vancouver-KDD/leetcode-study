from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        connected_components = 0

        for node in range(n):
            if node not in visited:
                connected_components += 1
                dfs(node)

        return connected_components

solution = Solution()
example1_n, example1_edges = 3, [[0, 1], [0, 2]]
example2_n, example2_edges = 6, [[0, 1], [1, 2], [2, 3], [4, 5]]

output1 = solution.countComponents(example1_n, example1_edges)
output2 = solution.countComponents(example2_n, example2_edges)
print(output1)
print(output2)
