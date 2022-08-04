class Solution {
public:
    bool dfs(vector<vector<char>>& board, int x, int y, string& word, int idx){
        
        if(idx==word.size()) return true;
        if(x<0 || x>=board.size() || y<0 || y>=board[0].size()) return false;
        if(board[x][y]=='.' || board[x][y]!=word[idx]) return false;
        
        char c = board[x][y];
        board[x][y] = '.';
        
        bool res = dfs(board,x+1,y,word,idx+1) || dfs(board,x-1,y,word,idx+1) || dfs(board,x,y+1,word,idx+1) || dfs(board,x,y-1,word,idx+1);
        
        board[x][y] = c;
        return res;
    }
    bool exist(vector<vector<char>>& board, string word) {
        for(int i=0; i<board.size(); i++){
            for(int j=0; j<board[0].size(); j++){
                if(dfs(board,i,j,word,0)) return true;
            }
        }
        return false;
    }
};