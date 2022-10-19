class Solution:
    def getGraph(self,  numCourses: int, prerequisites: List[List[int]]) \
    -> Tuple[Dict[int, List[int]], List[int]]:
        in_deg = [0] * numCourses
        course_g = {}
        
        for cur, pre in prerequisites:
            course_g[pre] = course_g[pre] + [cur] if pre in course_g else [cur]
            in_deg[cur] += 1
            
        return course_g, in_deg
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visit = [False] * numCourses
        stack = []

        course_g, in_deg = self.getGraph(numCourses, prerequisites)
        
        # add vertex which has 0 in-degree
        for vertex in range(len(in_deg)):
            if in_deg[vertex] == 0:
                stack.append(vertex)
        
        # operate while there is vertex with 0 in-degree
        while stack:
            vertex = stack.pop()
            visit[vertex] = True # mark to visit

            if vertex in course_g:
                for out_v in course_g[vertex]:
                    in_deg[out_v] -= 1 # get rid of in-degree of destination vertex
                    if in_deg[out_v] == 0:
                        stack.append(out_v)
                        
        # check there is a vertex with non 0 in-degree
        for deg in in_deg:
            if deg > 0:
                return False
            
        return True
