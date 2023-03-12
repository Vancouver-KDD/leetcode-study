"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
## Cycle!

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
class Solution:
    # O(n + p) where p = len(prerequisites)
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # course / prerequisites -> hashmap
        # dfs on each node to find how many courses it can take
        # if prerequisites == [], we are able to complete the node of course
        # remove prerequisites from the list when we know that the course can be completed
        # To detect cycle, use visitSet (recording the visited course(=node)) but when we run into something is already in the visitSet, that means it's a loop

        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        # visitSet = all courses along the curr DFS path
        visit_set = set()

        def dfs(crs):
            if crs in visit_set:    # Cycle = loop
                return False
            if pre_map[crs] == []:
                return True

            visit_set.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visit_set.remove(crs)
            pre_map[crs] = []   # preventing from repeating the same dfs path again
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
