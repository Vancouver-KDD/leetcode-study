// There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
// You are given an array prerequisites where prerequisites[i] = [ai, bi]
// indicates that you must take course bi first if you want to take course ai.

// For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
// Return true if you can finish all courses. Otherwise, return false.

// Input: numCourses = 2, prerequisites = [[1,0]]
// Output: true
// Explanation: There are a total of 2 courses to take. 
// To take course 1 you should have finished course 0. So it is possible.

// using DFS from each border cell to check which cells can flow to both the Pacific and Atlantic oceans
// time complexity is O(MN): M and N are the dimensions of the island as we visit each cell once during the DFS search
// space complexity is O(MN): two 2D boolean arrays to store whether a cell can flow to each ocean
class Solution {
    int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> result = new ArrayList<>();
        if (heights == null || heights.length == 0 || heights[0].length == 0) {
            return result;
        }
        int m = heights.length, n = heights[0].length;
        boolean[][] canReachPacific = new boolean[m][n];
        boolean[][] canReachAtlantic = new boolean[m][n];
        
        // check cells that can flow to Pacific Ocean
        for (int i = 0; i < m; i++) {
            dfs(heights, canReachPacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(heights, canReachPacific, 0, j);
        }
        
        // check cells that can flow to Atlantic Ocean
        for (int i = 0; i < m; i++) {
            dfs(heights, canReachAtlantic, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(heights, canReachAtlantic, m - 1, j);
        }
        
        // check cells that can flow to both oceans
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (canReachPacific[i][j] && canReachAtlantic[i][j]) {
                    List<Integer> cell = new ArrayList<>();
                    cell.add(i);
                    cell.add(j);
                    result.add(cell);
                }
            }
        }
        return result;
    }
    
    private void dfs(int[][] heights, boolean[][] canReachOcean, int i, int j) {
        int m = heights.length, n = heights[0].length;
        canReachOcean[i][j] = true;
        for (int[] direction : directions) {
            int x = i + direction[0], y = j + direction[1];
            if (x < 0 || x >= m || y < 0 || y >= n || canReachOcean[x][y] || heights[x][y] < heights[i][j]) {
                continue;
            }
            dfs(heights, canReachOcean, x, y);
        }
    }
}
