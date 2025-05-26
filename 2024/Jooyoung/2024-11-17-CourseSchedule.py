from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            adj_list[b].append(a)
            in_degree[a] += 1

        zero_in_degree = deque([i for i in range(numCourses) if in_degree[i] == 0])
        courses_taken = 0

        while zero_in_degree:
            course = zero_in_degree.popleft()
            courses_taken += 1
            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_in_degree.append(neighbor)

        return courses_taken == numCourses

solution = Solution()
example1_numCourses, example1_prerequisites = 2, [[0, 1]]
example2_numCourses, example2_prerequisites = 2, [[0, 1], [1, 0]]

output1 = solution.canFinish(example1_numCourses, example1_prerequisites)
output2 = solution.canFinish(example2_numCourses, example2_prerequisites)
print(output1)
print(output2)
