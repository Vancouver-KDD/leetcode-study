from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = {i:[] for i in range(numCourses)}
        inDegrees = {i:0 for i in range(numCourses)}

        for pre in prerequisites:
            inDegrees[pre[1]] += 1
            edges[pre[0]].append(pre[1])

        sources = deque()
        for i in range(numCourses):
            if inDegrees[i] == 0:
                sources.append(i)

        ans = []
        while sources:
            cur = sources.popleft()
            ans.append(cur)

            for child in edges[cur]:
                inDegrees[child] -= 1
                if inDegrees[child] == 0:
                    sources.append(child)

        return ans[::-1] if len(ans) == numCourses else []