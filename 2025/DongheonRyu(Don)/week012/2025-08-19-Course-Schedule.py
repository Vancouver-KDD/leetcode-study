def canFinish(numCourses, prerequisites):
    graph = {}
    for i in range(numCourses):
        graph[i] = []
    indegree = [0] * numCourses

    for crs, pre in prerequisites:
        graph[pre].append(crs)
        indegree[crs] += 1

    queue = []
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    taken = 0
    while queue:
        course = queue.pop(0)
        taken += 1
        for nei in graph[course]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return taken == numCourses
