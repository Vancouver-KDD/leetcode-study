class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        for (const auto& prereq : prerequisites) {
            graph[prereq[1]].push_back(prereq[0]);
        }

        vector<int> visited(numCourses, 0); // 0: 미방문, 1: 방문 중, 2: 방문 완료

        for (int i = 0; i < numCourses; ++i) {
            if (visited[i] == 0) {
                if (!dfs(i, graph, visited)) return false;
            }
        }

        return true;
    }

    bool dfs(int course, const vector<vector<int>>& graph, vector<int>& visited) {
        if (visited[course] == 1) return false;
        if (visited[course] == 2) return true;

        visited[course] = 1; // 방문중
        for (int neighbor : graph[course]) {
            if (!dfs(neighbor, graph, visited)) return false;
        }
        visited[course] = 2; // 방문 완료
        return true;
    }
};