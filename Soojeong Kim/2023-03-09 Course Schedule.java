//DFS
import java.util.*;
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        ArrayList[] graph = new ArrayList[numCourses];
        //make arraylist for each graph
        for(int i = 0; i<numCourses;i++) {
            graph[i] = new ArrayList();
        }
        boolean[] visited = new boolean[numCourses];
        boolean [] dp = new boolean[numCourses];
        for(int i = 0; i<prerequisites.length;i++) {
            //class you take first
            graph[prerequisites[i][1]].add(prerequisites[i][0]);
        }
        
        for(int i = 0;i<numCourses;i++) {
            if(!dfs(graph,visited, i, dp)) return false;
        }
        return true;
    }

    private boolean dfs(ArrayList[] graph, boolean [] visited, int index, boolean[] dp) {
        if(visited[index]) {
            return dp[index];
        }else {
            visited[index] = true;
        }

        for(int i = 0; i<graph[index].size();i++) {
            if(!dfs(graph, visited, (int)graph[index].get(i), dp)) {
                dp[index] = false;
                return false;
            }
        }

        dp[index] = true; //to mark down visited index status
        return true;
    }
}
//TLE : backtrack the visited array -> use another array to track 
//In your DFS solution, you are resetting the visited array every time you finish with a node.
//You're using it as a temporary visited array. This means if you visit a sub node of a visited node, you're doing excess work for no reason. 
//I believe you need another permanent visited array to prevent this.
//Time complexity : time complexity O(2^N),space complexity O(N)

//BFS
class Solution2 {
    //bfs
    public boolean canFinish(int numCourses, int[][] prerequisites) {
       ArrayList[] graph = new ArrayList[numCourses];
       int [] degree = new int[numCourses];
       Queue q = new LinkedList<>();
       int count = 0; //to check how many classes

       for(int i = 0; i<numCourses;i++) {
           graph[i] = new ArrayList();
       }

       for(int i = 0; i<prerequisites.length;i++) {
           //count if there is a class you need to take first
           degree[prerequisites[i][1]]++;
           graph[prerequisites[i][0]].add(prerequisites[i][1]);
       }
        for(int i = 0; i<degree.length;i++) {
            if(degree[i]==0){
                q.add(i);// class that doesn't have any requirements.
                count++;
            }
        }
        while(!q.isEmpty()) {
            int course = (int)q.poll();
           //go through the classes which has this course as a requirement 
            for(int i = 0; i<(int)graph[course].size();i++) {
                int pointer = (int)graph[course].get(i);
                degree[pointer]--;
                if(degree[pointer] == 0) {
                    q.add(pointer);
                    count++;
                }
            }
        }
        return count==numCourses? true : false;
    }
}
