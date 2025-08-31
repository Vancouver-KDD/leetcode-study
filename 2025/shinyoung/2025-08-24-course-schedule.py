from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        # Time: O(N + E)
        # Space: O(N + E)
        
        g = defaultdict(list)
        courses = prerequisites
        for a, b in courses:
            g[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITIED = 2

        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]
            if state == VISITIED:
                return True
            elif state == VISITING:
                return False

            states[node] = VISITING

            for nei in g[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITIED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


solution = Solution()
print(solution.canFinish(numCourses=2, prerequisites=[[1, 0]]))
print(solution.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
