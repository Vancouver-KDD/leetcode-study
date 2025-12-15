
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # edge: b -> a (take b before a)
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        taken = 0
        while q:
            course = q.popleft()
            taken += 1
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return taken == numCourses