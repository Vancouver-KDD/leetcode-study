// There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
// You are given an array prerequisites where prerequisites[i] = [ai, bi] 
// indicates that you must take course bi first if you want to take course ai.

// For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
// Return true if you can finish all courses. Otherwise, return false.

// Input: numCourses = 2, prerequisites = [[1,0]]
// Output: true
// Explanation: There are a total of 2 courses to take. 
// To take course 1 you should have finished course 0. So it is possible.

// 03/04 - need to be reviewed
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        int[] inDegree = new int[numCourses];
        Queue<Integer> queue = new LinkedList<>();
        int numFinishedCourses = 0;
        
        // initialize adjacency list and in-degree counts
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] prerequisite : prerequisites) {
            graph.get(prerequisite[1]).add(prerequisite[0]);
            inDegree[prerequisite[0]]++;
        }
        
        // add all courses with in-degree 0 to queue
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }
        
        // process courses in queue and update in-degree counts
        while (!queue.isEmpty()) {
            int course = queue.poll();
            numFinishedCourses++;
            for (int adjCourse : graph.get(course)) {
                inDegree[adjCourse]--;
                if (inDegree[adjCourse] == 0) {
                    queue.offer(adjCourse);
                }
            }
        }
        
        // check if all courses have been finished
        return numFinishedCourses == numCourses;
    }
}
