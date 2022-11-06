class Solution {
    public boolean exist(char[][] board, String word) {
        for(char c : word.toCharArray()) {
            boolean exist = false;
            for(int x = 0; x < board.length; x++) {
                for(int y = 0; y < board[0].length; y++) {
                    if(board[x][y] == c) {
                        exist = true;
                        break;
                    }
                }
            }
            if(!exist) return false;
        }
        boolean[][] visit = new boolean[board.length][board[0].length];
        for(int x = 0; x < board.length; x++) {
            for(int y = 0; y < board[0].length; y++) {
                if(helper(board, x, y, word, 0, visit)) return true;
            }
        }
        return false;
    }

    private boolean helper(char[][] board, int x, int y, String word, int wordIdx, boolean[][] visit) {
        if(x < 0 || x > board.length-1) return false;
        if(y < 0 || y > board[0].length-1) return false;
        if(visit[x][y]) return false;

        if(board[x][y] == word.charAt(wordIdx)) {
            if(wordIdx == word.length()-1) return true;
            visit[x][y] = true;
            // up
            if(helper(board, x, y+1, word, wordIdx+1, visit)) return true;
            // down
            if(helper(board, x, y-1, word, wordIdx+1, visit)) return true;
            // right
            if(helper(board, x+1, y, word, wordIdx+1, visit)) return true;
            // left
            if(helper(board, x-1, y, word, wordIdx+1, visit)) return true;
        }
        visit[x][y] = false;
        return false;
    }
}