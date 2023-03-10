import java.util.*;
class Solution {
    List<List<Integer>> result;
    boolean [][] pacific;
    boolean [][] atlantic;
    //int [][] move = new int[][] {{0,1}, {0,-1}, {1, 0}, {-1, 0}};
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int c = heights.length;
        int h = heights[0].length;
        result = new ArrayList<>();
        pacific = new boolean[c][h];
        atlantic = new boolean[c][h];
        //1보다는 크니까 그건 생각할 필요 없음
        //사방으로 닿는 면 true 처리해주기
        for(int i = 0; i<c;i++) {
            dfs(heights, pacific, Integer.MIN_VALUE, i, 0);
            dfs(heights, atlantic, Integer.MIN_VALUE, i, h-1);
        }
        for(int i = 0; i<h;i++) {
            dfs(heights, pacific, Integer.MIN_VALUE, 0, i);
            dfs(heights, atlantic, Integer.MIN_VALUE, c-1, i);
        }

        for(int i = 0; i<c;i++) {
            for(int j = 0; j<h;j++){
                if(pacific[i][j] && atlantic[i][j]) {
                    result.add( new ArrayList<>(Arrays.asList(i,j)) );
                }
            }
        }
        return result;
    }
    private void dfs(int[][] heights, boolean[][] visited, int height, int i, int j) {
        int c = heights.length;
        int h = heights[0].length;
        if(i<0 || i>=c || j<0 || j>=h || visited[i][j] || heights[i][j]<height) {
            return;
        }
        visited[i][j] = true;
        dfs(heights, visited, heights[i][j], i, j+1);
        dfs(heights, visited, heights[i][j], i, j-1);
        dfs(heights, visited, heights[i][j], i+1, j);
        dfs(heights, visited, heights[i][j], i-1, j);
    }
}
//O(m*N)