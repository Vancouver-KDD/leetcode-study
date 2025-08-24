function canFinish(numCourses: number, prerequisites: number[][]): boolean {
  const graph: number[][] = Array.from({ length: numCourses }, () => []);
  for (const [course, prereq] of prerequisites) {
    graph[prereq].push(course);
  }

  const visited: number[] = new Array(numCourses).fill(0);

  function dfs(course: number): boolean {
    if (visited[course] === 1) return false;
    if (visited[course] === 2) return true;

    visited[course] = 1;
    for (const next of graph[course]) {
      if (!dfs(next)) return false;
    }
    visited[course] = 2;
    return true;
  }

  for (let i = 0; i < numCourses; i++) {
    if (!dfs(i)) return false;
  }

  return true;
}
