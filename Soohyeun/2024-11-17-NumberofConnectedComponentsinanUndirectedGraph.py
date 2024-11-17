import collections

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # create graph -> bfs, remove nodes until graph gets empty

        # create graph
        connection = {i: set() for i in range(n)}
        for a, b in edges:
            connection[a].add(b)
            connection[b].add(a)

        components = 0
        unvisited = {i for i in range(n)}
        q = collections.deque()

        while unvisited:
            q.append(unvisited.pop())
            components += 1
            while q:
                curr_node = q.pop()

                for neighbour in connection[curr_node]:
                    connection[neighbour].remove(curr_node)
                    if neighbour in unvisited:
                        unvisited.remove(neighbour)
                        q.append(neighbour)

        return components
