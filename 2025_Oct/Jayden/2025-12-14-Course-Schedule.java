class Solution {
    /*
        Let V = numCourses
        Let E = pprerequisites.length
        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
     */
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();

        // Represents many prerequisites each course (index) needs to take
        int[] prerequisitesCount = new int[numCourses];

        // Initialize the adjacency list for all courses
        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }

        // Building graph
        for (int[] prerequisite : prerequisites) {
            int course = prerequisite[0];
            int requiredCourse = prerequisite[1]; // course that must take first

            // requiredCourse -> course
            adj.get(requiredCourse).add(course);

            // This course now has one more prerequisite
            prerequisitesCount[course]++;
        }

        // Represents the courses that have no remaining prerequidites
        Queue<Integer> readyCourses = new LinkedList<>();

        // Add all courses have no prerequisites
        for (int i = 0; i < numCourses; i++) {
            if (prerequisitesCount[i] == 0) readyCourses.offer(i);
        }

        int completedCourses = 0;

        while (!readyCourses.isEmpty()) {
            int currentCourse = readyCourses.poll();
            completedCourses++;

            // For every course that depended on the current one
            for (int dependentCourse : adj.get(currentCourse)) {
                prerequisitesCount[dependentCourse]--;

                // If all prerequisites are now satisfied
                if (prerequisitesCount[dependentCourse] == 0) {
                    readyCourses.offer(dependentCourse);
                }
            }
        }

        return completedCourses == numCourses;
    }
}