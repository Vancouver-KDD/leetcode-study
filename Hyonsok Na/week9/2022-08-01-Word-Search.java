class Solution {

    private int row;
    private int col;
    private boolean[][] visited;
    private boolean result = false;
    public boolean exist(char[][] board, String word) {
    
        row = board.length;
        col = board[0].length;
        visited = new boolean[row][col];
        
        for(int i = 0; i < row; i++) {
            for(int j = 0; j < col; j++) {
                if(board[i][j] == word.charAt(0)) {
                    DFS(i, j, board, word, 0);                    
                }
            }
        }
        
    return result;    
    }
    
    public void DFS(int i, int j, char[][] board, String word, int idx) {
        
        if(i < 0 || j < 0 || i >= row || j >= col) return;
        if(visited[i][j] == true || idx >= word.length()) return;
        if(word.charAt(idx) != board[i][j]) return;
        
        if(idx == word.length() - 1) {
            result = true;
            return;
        }
        
        visited[i][j] = true;
        idx++;
        
        DFS(i-1, j, board, word, idx);
        DFS(i+1, j, board, word, idx);
        DFS(i, j+1, board, word, idx);
        DFS(i, j-1, board, word, idx);    
        
        visited[i][j] = false;
    }
}