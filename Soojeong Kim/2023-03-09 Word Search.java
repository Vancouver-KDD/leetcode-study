class Solution {
    static boolean result;
    public boolean exist(char[][] board, String word) {
        int c = board.length;
        int h = board[0].length;
        result = false;
        
        for(int i =0 ; i<c;i++) {
            for(int j = 0;j<h;j++) {
                if(board[i][j] == word.charAt(0)) {
                    dfs(i, j, word, board, 0);
                    if(result) return true;
                }
            }
        }
        return false;
    }
    private void dfs(int i, int j, String word, char[][] board, int index) {
         if(word.length() == index) {
            result = true;
            return;
        }
        if(i>=board.length || j>=board[0].length || i<0 || j<0 || board[i][j] != word.charAt(index) ) return;
        
        char temp = board[i][j];
        board[i][j] = '#';
        dfs(i, j+1, word, board, index+1);
        dfs(i+1, j, word, board, index+1);
        dfs(i-1, j, word, board, index+1);
        dfs(i, j-1, word, board, index+1);
        board[i][j] = temp;

    }
}

//space : O(L) - L is length of a word
//time : O(M*N*4^L) board(M)(N)