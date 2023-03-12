"""
323. Number of Connected Components in an Undirected Graph
"""

class Solution:

    def validTree(self, n: int, edges) -> bool:
        # Requirements:
        # Any two vertices should be connected
        # No cycle

        # Graph -> DFS -> num_visited == n True
        # Find cycle use state while DFS

        # Create adjacency list
        # Create the adjacency list for the graph
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # Keep track of the visited vertices
        visited = set()

        # Define the DFS function
        def dfs(v, parent):
            # If v is already visited, then there is a cycle
            if v in visited:
                return False

            # visite the node
            visited.add(v)

            for neighbor in graph[v]:
                if neighbor != parent:
                    if not dfs(neighbor, v):
                        return False

            return True

        # Check if all nodes are visited

        # Version 1
        # # Perform DFS on all unvisited nodes
        # for node in range(n):
        #     if node not in visited:
        #         if not dfs(node, -1):
        #             return False
        # return len(visited) == n

        # version 2
        return dfs(0, -1) and len(visited) == n


def main():
    s = Solution()


if __name__ == "__main__":
    main()
