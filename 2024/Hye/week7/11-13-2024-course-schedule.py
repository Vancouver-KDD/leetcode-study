class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        1. build directed graph: graph[prerequisite] = nex_course
        2. Build in_degree array to get the number of prerequisite required for the course
        3. BFS through courses starting from first prerequisite (in_degree = 0)
        """
        # Build neighbouring graph and in_degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Build starting queue with 0 in_degree node
        queue = deque()
        for course, num_preq in enumerate(in_degree):
            if in_degree[course] == 0:
                queue.append(course)
        
        visited = set()
        # BFS
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for nei in graph[node]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0:
                        queue.append(nei)
        
        return len(visited) == numCourses
