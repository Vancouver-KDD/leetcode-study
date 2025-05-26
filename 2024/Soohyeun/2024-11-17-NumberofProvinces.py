from collections import deque
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        visited = set()
        n = len(isConnected)
        provinces = 0

        def bfs(city):
            q = deque([city])
            visited.add(city)
            while q:
                curr_city = q.popleft()
                for neighbour, connect in enumerate(isConnected[curr_city]):
                    if connect and neighbour not in visited:
                        q.append(neighbour)
                        visited.add(curr_city)

        for i in range(n):
            if i not in visited:
                provinces += 1
                bfs(i)

        return provinces
