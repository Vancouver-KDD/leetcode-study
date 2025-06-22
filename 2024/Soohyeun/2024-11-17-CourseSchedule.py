class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [a, b]: b -> a
        # Create graph
        graph = {i: [] for i in range(numCourses)}
        indegrees = [0] * numCourses
        d = deque()
        visited = set()
        for des, src in prerequisites:
            graph[src].append(des)
            indegrees[des] += 1

        # find root
        for index, indegree in enumerate(indegrees):
            if indegree == 0:
                d.append(index)

        # check graph
        while d:
            course = d.popleft()
            visited.add(course)
            for node in graph[course]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    d.append(node)

        return len(visited) == numCourses
