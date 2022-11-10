//leetcode solution
//Time complexity : O(Nx3^L) : N is the number of cells in the board and L is the length of the word to be matched.
//Space complexity : O(L) : L is the length of the word to be matched.

//2022.11.06
class Solution{
    public boolean exist(char[][] board, String word){
        boolean isExist = false;
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(checkBoard(board, word, 0, i, j)){
                    return true;
                }
            }
        }
        return isExist;
    }

    private boolean checkBoard(char[][] board, String word, int wordPos, int bi, int bj){
            if(wordPos == word.length()){
                return true; // end of string
            }
            if( bi < 0 || bi >= board.length || bj < 0 || bj >= board[0].length){
                return false; // out of boundary
            }

            if(board[bi][bj] != word.charAt(wordPos)){
                return false;
            }

            char ch = board[bi][bj];
            board[bi][bj] = '#'; //marked - visited
            //recursive function
            if(checkBoard(board, word, wordPos+1, bi-1, bj)){ //up
                return true;
            }
            if(checkBoard(board, word, wordPos+1, bi+1, bj)){ //down
                return true;
            }
            if(checkBoard(board, word, wordPos+1, bi, bj-1)){//left
                return true;
            }
            if(checkBoard(board, word, wordPos+1, bi, bj+1)){//right
                return true;
            }
            
            board[bi][bj] = ch; //recover 
            return false;
    }
}