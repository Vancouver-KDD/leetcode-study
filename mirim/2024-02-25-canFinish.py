# https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        graph = collections.defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        indegrees = [False] * numCourses
        for prereq, _ in prerequisites:
            indegrees[prereq] += 1

        q = collections.deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)

        while q:
            cur_v = q.popleft()
            for prereq in graph[cur_v]:
                indegrees[prereq] -= 1
                if indegrees[prereq] == 0:
                    q.append(prereq)

        return all(indegree == 0 for indegree in indegrees)
