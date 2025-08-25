class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        We need to detect a loop in the list of prereqs
        Build a graph with the pre-reqs and then if we detect loop while we are traversing graph with backtracking algo, we return false. We need to try start traversal at all vertex of the graph
        
        we can build a graph via adjacency list (implemented with Dict)
            -> each vertex is a pre-req and all its neighbors are the courses u can take after finish that pre-req


        To traverse the graph, we can use DFS + backtracking:
        1. when we see a node, need to see if its been visited before. if it has been vistied
            * if its part of current stack we build from visiting, then its a loop
            * else, its just a node that we have visited from other stack, we can skip it as the other stack doesn't result in a loop, return F
        2. now that we know the node has not been visited, we can mark it as visited and add it to visitStack and visit all its neighbors by iterating through the adjaceny list
        3. As soon as we find a loop, we would return T, and we only need one T to dictate that we found a loop,
        4. Hence, we can use the format return (findLoop(neihgbor 1) or findLoop(neighbor2) ... ). Note, keep in mind we need to backtrack whenever we are done visiting a neighbor by removing that neighbor from visitStack before we visit the next neighbor

        5. After we finish findLoop, we need to negate the result as finding lopop just means we can't finish all the courses
        '''

        # Building the graph
        graph = {}
        for i in range(len(prerequisites)):
            course, prereq = prerequisites[i]
            if prereq not in graph:
                graph[prereq] = []
            graph[prereq].append(course)
        

        # traverse the graph
        def findLoop(node, visitStack, visited):
            if node in visited:
                if node in visitStack:
                    return True
                else:
                    return False
            if node not in graph:
                visited.add(node)
                return False

            visited.add(node)
            visitStack.add(node)
            for i in range(len(graph[node])):
                neighbor = graph[node][i]
                if findLoop(neighbor, visitStack, visited):
                    return True
                
            visitStack.remove(node)
            return False
        

        visitStack = set()
        visited = set()
        for node in graph.keys():
            if findLoop(node, visitStack, visited):
                return False
        
        return True
                    

