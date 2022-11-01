class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this is essentially checking cycle using hashmap and set
        
        # Create a {course: [prereq]} mapping
        prereqMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        
        # visitSet is a cycle to check whether you visit same course again in current traverse
        visitSet = set()
        
        
        def dfs(course:int) -> bool:
            
            # if current dfs is visiting the same course twice, return False
            if course in visitSet:
                return False
            
            # if current course has no prereqs to visit, return True
            if prereqMap[course] == []:
                return True
            
            # add current course to visiting courses
            visitSet.add(course)
            
            # visit prereqs of current course and check cycle 
            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
            
            # if the dfs reached this point, it means that there is no cycle starting from 'course'
            # which in other words, you can take 'course' fulfiling all its prereqs
            
            # you are done with visting 'course' and its prereqs
            visitSet.remove(course)
            
            # mark current course as possible to finish by emptying prereq list
            prereqMap[course] = []
            
            return True
        
        
        # if you find any cycle starting from any course, return False immediately
        for c in range(numCourses):
            if not dfs(c):
                return False
        # if there is no cycle starting from any courses in the course list, return true
        return True
            
            