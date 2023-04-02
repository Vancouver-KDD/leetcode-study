"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges

Input: n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
"""
class Solution:
    # O(E+V)
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # Trees are not allowed to have a loop
        # All nodes have to be connected (verified node # = visited node)
        if not n:
            return True

        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # for the example of edges = [[0,1], [0,2], [0,3], [1,4]]
        # adj = {0: [1, 2, 3], 1: [4]}

        visit = set()

        def dfs(i, prev):
            if i in visit:  # loop
                return False
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):   # loop; the parent node is the child node of its child node
                    return False
            return True

        return dfs(0, -1) and n == len(visit)  # start from node 0, -1 is not going to be in our input