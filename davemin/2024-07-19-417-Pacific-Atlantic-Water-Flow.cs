
public class Solution {
    public IList<IList<int>> PacificAtlantic(int[][] heights) {
        HashSet<(int,int)> pac = new HashSet<(int,int)>();
        HashSet<(int,int)> atl = new HashSet<(int,int)>();
        List<IList<int>> result = new List<IList<int>>();

        int rows = heights.Length;
        int cols = heights[0].Length;

        void dfs(int r,int c, HashSet<(int,int)> visited, int prev){
            if(r<0 || c<0 || r==rows || c==cols || visited.Contains((r,c)) || prev > heights[r][c]){
                return;
            }
            visited.Add((r,c));
            dfs(r+1,c,visited, heights[r][c]);
            dfs(r-1,c,visited, heights[r][c]);
            dfs(r,c+1,visited, heights[r][c]);
            dfs(r,c-1,visited, heights[r][c]);
        }
        for(int c=0;c<cols;c++){
            dfs(0,c,pac,heights[0][c]);
            dfs(rows-1,c,atl,heights[rows-1][c]);
        }
        for(int r=0;r<rows;r++){
            dfs(r,0,pac,heights[r][0]);
            dfs(r,cols-1,atl,heights[r][cols-1]);
        }
        for(int r=0;r<rows;r++){
            for(int c=0;c<cols;c++){
                if(pac.Contains((r,c)) && atl.Contains((r,c))){
                    result.Add(new List<int>(){r,c});
                }
            }
        }
        return result;
    }
}
