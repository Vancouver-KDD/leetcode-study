"""
323. Number of Connected Components in an Undirected Graph
"""

class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build adjacecny list

        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        components = 0
        for vertex in range(n):
            if not visited[vertex]:
                self.dfs(graph, vertex, visited)
                components += 1

        return components

    def dfs(self, graph, start, visited):
        visited[start] = True
        for neighbour in graph[start]:
            if not visited[neighbour]:
                self.dfs(graph, neighbour, visited)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
