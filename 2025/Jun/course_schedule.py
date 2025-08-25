class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        states = [0] * numCourses
        hashmap = defaultdict(list)
        for course, pre in prerequisites:
            hashmap[course].append(pre)

        def dfs(course):
            if states[course] == 2:
                return True
            if states[course] == 1:
                return False
            states[course] = 1
            for pre in hashmap[course]:
                if not dfs(pre):
                    return False
            states[course] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True