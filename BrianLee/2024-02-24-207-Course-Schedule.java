https://leetcode.com/problems/course-schedule/description/

class Solution {
    /* 위상 정렬(Topology Sort)
     노드로 들어오는 엣지의 수(indegree)
     노드에서 나가는 엣지의 수(outdegree)

     풀이
     0. 루프 시작
     1. indegree == 0 탐색
     2. 그 노드의 관련 outdegree 제거, indegree 업데이트
     3. 1,2번 반복
     4. 푸르 종료 후 모든 노드를 탐색했는지 확인
    */
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        List<List<Integer>> adjList = new ArrayList<>();

        for(int i = 0; i < numCourses; i++) adjList.add(new ArrayList<Integer>());

        // edge[1] => edge[0]
        for(int[] edge: prerequisites) {
            indegree[edge[0]]++;
            adjList.get(edge[1]).add(edge[0]);
        }

        // Like BFS Search
        // 1. indegree == 0 탐색
        Queue<Integer> q = new LinkedList<>();
        for(int i=0; i < numCourses; i++) {
            if(indegree[i]==0) q.offer(i);
        }

        Set<Integer> visited = new HashSet<>();
        while(!q.isEmpty()) {
            int node = q.poll();
            visited.add(node);
            for(int dest: adjList.get(node)) {
                // 2. 그 노드의 관련 outdegree 제거, indegree 업데이트
                if(--indegree[dest] == 0) q.offer(dest);
            }
            // 필요X adjList.get(node).clear();
        }
        return visited.size() == numCourses;
    }
}