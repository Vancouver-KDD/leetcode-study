import java.util.*;

class CourseSchedule {
    private List<Integer>[] graph;
    private int[] visited;

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        graph = new ArrayList[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] pre : prerequisites) {
            graph[pre[1]].add(pre[0]);
        }

        visited = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (visited[i] == 0 && !dfs(i)) {
                return false;
            }
        }
        return true;
    }

    private boolean dfs(int course) {
        if (visited[course] == 1) return false;
        if (visited[course] == 2) return true;

        visited[course] = 1;
        for (int next : graph[course]) {
            if (!dfs(next)) return false;
        }
        visited[course] = 2;
        return true;
    }
}
