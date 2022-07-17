class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Create prereqMap
        prereqMap = {i:[] for i in range(numCourses)}
        
        
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        
        # Set of visited vertices in current DFS  
        visitSet = set()
        
        def dfs(course):
            if course in visitSet:
                return False
            
            if prereqMap[course] == []:
                return True
            
            visitSet.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
            visitSet.remove(course)
            prereqMap[course] = []    
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True