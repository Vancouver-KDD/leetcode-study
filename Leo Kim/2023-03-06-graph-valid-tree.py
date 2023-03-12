class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        root = [i for i in range(n)]
        rank = [1 for i in range(n)]
        count = n

        def find(x):
            # Find using path compression
            if (root[x] == x): return x
            root[x] = find(root[x])
            return root[x]

        def union(x, y):
            # Union using union by rank
            rootX = find(x)
            rootY = find(y)
            if (rootX != rootY):
                if (rank[rootX] > rank[rootY]): root[rootY] = rootX
                if (rank[rootY] > rank[rootX]): root[rootX] = rootY
                if (rank[rootY] == rank[rootX]):
                    root[rootX] = rootY
                    rank[rootY] -= 1
                return True
            return False

        # Build up our disjoint set
        for edge in edges:
            x = union(edge[0], edge[1])
            if (not x): return False
            if (x): count -= 1
        print(count, root)

        if (count > 1): return False
        return True