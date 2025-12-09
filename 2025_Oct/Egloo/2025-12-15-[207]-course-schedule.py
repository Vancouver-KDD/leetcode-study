class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        g = dict()
        for c, p in prerequisites:
            if c not in g:
                g[c] = []
            g[c].append(p)
        
        visited = [] 
        
        def check(course, origin):
            if course == origin and visited[course] == 1:
                return False

            if visited[course] == 1 or course not in g:
                return True

            visited[course] = 1

            for p in g[course]:
                r = check(p, origin)
                if not r:
                    return r

            return True

        for c in g:
            visited = [0 for _ in range(numCourses)] 
            if not check(c, c):
                return False

        return True

            
