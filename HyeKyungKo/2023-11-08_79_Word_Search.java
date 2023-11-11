

//2023-11-07
//BackTracking
//Time Complexity: O(M*N * 3^L) , M*N = the number of cells, L is length of string
//Space Complexity: O(L) , recursive call stack size = string length 만큼 call
class Solution{
    public boolean exist(char[][] board, String word){
        if(board == null || board.length <= 0 || word == null || word.length() <= 0){
            return false;
        }
        
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length; j++){
                if(backTracking(board, i,j,word, 0)){
                    return true;
                }
            }
        }
        return false;
        
    }
    
    boolean backTracking(char[][] board, int i, int j, String word, int pos){
        
        if(pos >= word.length()){
            return true;
        }
        if(i < 0 || i >= board.length || j < 0 || j >= board[0].length){
            return false;
        }
        
        char ch = word.charAt(pos);
        
        if(board[i][j] != ch){ // board[i][j] == '#' || board[i][j] != ch 두경우 모두포함됨.
            return false;
        }
        
        char savedCh = board[i][j];
        board[i][j] = '#';        

        if(backTracking(board, i-1, j, word, pos+1)){
            return true;
        }
        if(backTracking(board, i, j-1, word, pos+1)){
            return true;
        }
        if(backTracking(board, i+1, j, word, pos+1)){
            return true;
        }
        if(backTracking(board, i, j+1, word, pos+1)){
            return true;
        }
        
        board[i][j] = savedCh;
        
        return false;
    }
}


//leetcode solution
//Time complexity : O(Nx3^L) : N is the number of cells in the board and L is the length of the word to be matched.
//Space complexity : O(L) : L is the length of the word to be matched.
//2022.12.05
//
/*
class Solution{
    public boolean exist(char[][] board, String word){
        if(board == null || board.length == 0 || board[0].length == 0 || word == null || word.length() == 0){
            return false;
        }

        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(findWord(board, word, 0, i, j)){
                    return true;
                }
            }
        }
        return false;
    }

    private boolean findWord(char[][] board, String word, int pos, int row, int col){
        //바운더리 먼저 체크하면  pos 가 word.length()인 경우인데 false 가 리턴되버림.
        //
        //if(row < 0 || row >= board.length || col < 0 || col >= board[0].length){
        //    return false;
        //}
        //

        if(pos == word.length()){
            return true;
        }

        if(row < 0 || row >= board.length || col < 0 || col >= board[0].length){
            return false;
        }

        char ch = word.charAt(pos);
        // 어차피 아래 if 문에 의해 return false 됨 
        //if(ch == '#'){
        //    return false;
        //}

        if(ch != board[row][col]){
            return false;
        }

        board[row][col] = '#'; //marked -visited
        if(findWord(board, word, pos+1, row-1, col)){
            return true;
        }
        if(findWord(board, word, pos+1, row+1, col)){
            return true;
        }
        if(findWord(board, word, pos+1, row, col-1)){
            return true;
        }
        if(findWord(board, word, pos+1, row, col+1)){
            return true;
        }

        board[row][col] = ch; //unmarked
        return false;
    }
}
*/
    
//2022.11.06
/*
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
*/
/*
class Solution {
    public boolean exist(char[][] board, String word) {
        if(word == null || word.length() == 0){
            return false;
        }
        
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(checkWord(board, word, i, j, 0)){
                    return true;
                }
            }
        }
        return false;
    }

    //check if there is the word on the board.
    private boolean checkWord(char[][] board, String word, int i, int j, int pos){
        
        if(pos >= word.length()){ // it means, there is the word in this board.
            return true;
        }
        
        if(i <0 || i >= board.length || j < 0 || j >= board[i].length){
            return false;
        }
        
        //if the character is same, search adjacent 4 direction 
        if(word.charAt(pos) == board[i][j]){
            //System.out.println("["+word.charAt(pos)+"]:"+i+", " +j);

            board[i][j] = '#';
            boolean r1 = false;
            boolean r2 = false;
            boolean r3 = false;
            boolean r4 = false;
           
            r1 = checkWord(board, word, i-1, j, pos+1);
            if(!r1){
                r2 = checkWord(board, word, i+1, j, pos+1);       
            }
            if(!r2){
               r3 = checkWord(board, word, i, j-1, pos+1);             
            }
            if(!r3){
                r4 = checkWord(board, word, i, j+1, pos+1);
            }

            board[i][j] = word.charAt(pos);
            return (r1 || r2 || r3 || r4 );
        }else{
            return false;
        }
        
    }
}
*/

//Limitation: word can be null??  return false? 

//Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED" ---> Output: true

//Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE" ---> Output: true

//Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB" ---> Output: false


//Time Complexity: O(NxMx3^L) : L 은 word 길이 ( word 각 character 마다 3방향을 체크해서 그런가?)
//Space Complexity: O(NxM)
/*
class Solution {
    public boolean exist(char[][] board, String word) {
        if(word == null || word.length() == 0){
            return false;
        }
        
        //define another board to check 'visit'
        int[][] visit = new int[board.length][board[0].length];
        
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(checkWord(board, word, i, j, 0, visit)){
                    return true;
                }
            }
        }
        return false;
    }
    
    //check if there is the word on the board.
    private boolean checkWord(char[][] board, String word, int i, int j, int pos, int[][] visit){
        if(i <0 || i >= board.length || j < 0 || j >= board[i].length || pos >= word.length()){
            return false;
        }
        
        //if the character is same, search adjacent 4 direction 
        if(word.charAt(pos) == board[i][j] && visit[i][j] != 1){
            //System.out.println("["+word.charAt(pos)+"]:"+i+", " +j);
            if(pos == word.length()-1){
                return true;
            }
            visit[i][j] = 1;
            boolean r1 = checkWord(board, word, i-1, j, pos+1, visit);
            boolean r2 = checkWord(board, word, i+1, j, pos+1, visit);
            boolean r3 = checkWord(board, word, i, j-1, pos+1, visit);
            boolean r4 = checkWord(board, word, i, j+1, pos+1, visit);
            visit[i][j] = 0;
            return (r1 || r2 || r3 || r4 );
        }else{
            return false;
        }
        
    }
}
*/