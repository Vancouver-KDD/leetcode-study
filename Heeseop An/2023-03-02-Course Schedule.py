class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = {i: [] for i in range(numCourses)}

        for course, preReqs in prerequisites:
            preReqMap[course].append(preReqs)

        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if preReqMap[course] == []:
                return True

            visited.add(course)
            for preReq in preReqMap[course]:
                if not dfs(preReq):
                    return False
            visited.remove(course)
            preReqMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
