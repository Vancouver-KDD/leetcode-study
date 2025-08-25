class PacificAtlanticWaterFlow {
    private int m, n;
    private int[][] heights;
    private boolean[][] pacific, atlantic;
    private int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        this.heights = heights;
        m = heights.length;
        n = heights[0].length;
        pacific = new boolean[m][n];
        atlantic = new boolean[m][n];

        for (int i = 0; i < m; i++) dfs(i, 0, pacific);
        for (int j = 0; j < n; j++) dfs(0, j, pacific);
        for (int i = 0; i < m; i++) dfs(i, n-1, atlantic);
        for (int j = 0; j < n; j++) dfs(m-1, j, atlantic);

        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    res.add(Arrays.asList(i, j));
                }
            }
        }
        System.out.println(Arrays.deepToString(pacific));
        System.out.println(Arrays.deepToString(atlantic));
        return res;
    }

    private void dfs(int i, int j, boolean[][] visited) {
        if (visited[i][j]) return;
        visited[i][j] = true;

        for (int[] d : dirs) {
            int x = i + d[0], y = j + d[1];
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            if (heights[x][y] < heights[i][j]) continue;
            dfs(x, y, visited);
        }
    }
}
