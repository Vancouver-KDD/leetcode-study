class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string> output;

        int rs = board.size();
        int cs = board[0].size();

        for (string& word : words) {
            bool found = false;
            for (int i = 0; i < rs && !found; i++) {
                for (int j = 0; j < cs; j++) {
                    if (board[i][j] == word[0]) {
                        if (BT(word, 0, board, i, j, rs, cs)) {
                            output.push_back(word);
                            found = true;
                            break;
                        }
                    }
                }
            }
        }
        return output;
    }

    bool BT(string& word, int idx, vector<vector<char>>& board, int r, int c, int& rs, int& cs) {
        if (idx == word.size())
            return true;
        if (r < 0 || c < 0 || r >= rs || c >= cs || board[r][c] != word[idx]) \
            return false;

        board[r][c] = '#';
        bool result = BT(word, idx + 1, board, r + 1, c, rs, cs) ||
                      BT(word, idx + 1, board, r - 1, c, rs, cs) ||
                      BT(word, idx + 1, board, r, c + 1, rs, cs) ||
                      BT(word, idx + 1, board, r, c - 1, rs, cs);
        board[r][c] = word[idx];
        return result;
    }
};
