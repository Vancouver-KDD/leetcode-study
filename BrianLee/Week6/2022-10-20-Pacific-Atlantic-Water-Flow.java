class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int[][] ocean = new int[heights.length][heights[0].length];
        // pacific
        int idx = 0;
        for(int i = 0; i < heights.length; i++) {
            dfs(heights, i, idx, ocean, 1, 0);
        }
        for(int i = 0; i < heights[0].length; i++) {
            dfs(heights, idx, i, ocean, 1, 0);
        }

        // atlantic
        idx = heights[0].length-1;
        for(int i = 0; i < heights.length; i++) {
            dfs(heights, i, idx, ocean, 2, 0);
        }
        idx = heights.length-1;
        for(int i = 0; i < heights[0].length; i++) {
            dfs(heights, idx, i, ocean, 2, 0);
        }

        List<List<Integer>> result = new ArrayList<>();
        for(int i = 0; i < heights.length; i++) {
            for(int j = 0; j < heights[0].length; j++) {
                if(ocean[i][j] == 3) {
                    List<Integer> point = new LinkedList<>();
                    point.add(i);
                    point.add(j);
                    result.add(point);
                }
            }
        }
        return result;
    }

    private void dfs(int[][] heights, int x, int y, int[][] ocean, int type, int preValue) {
        if(x >= 0 && x < heights.length && y >= 0 && y < heights[0].length) {
            if(ocean[x][y] < type && preValue <= heights[x][y]) {
                ocean[x][y] += type;
                // up
                dfs(heights, x-1, y, ocean, type, heights[x][y]);
                // down
                dfs(heights, x+1, y, ocean, type, heights[x][y]);
                // right
                dfs(heights, x, y+1, ocean, type, heights[x][y]);
                // left
                dfs(heights, x, y-1, ocean, type, heights[x][y]);
            }
        }
    }
}