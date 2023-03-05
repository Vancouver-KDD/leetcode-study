import java.util.*;

class Solution {
    class TrieNode {
        TrieNode [] childs = new TrieNode[26];
        String word;
    }

    public List<String> findWords(char[][] board, String[] words) {
        //dfs로 찾기
        List<String> result = new ArrayList<>();
        TrieNode root = buildTrie(words);
   
        for(int i = 0;i<board.length;i++) {
            for(int j = 0; j<board[0].length;j++) {
                dfs(board, i, j, root, result);
            }
        }
        return result;
    }

    private void dfs(char[][] board, int i, int j, TrieNode p, List<String> result) {
        char ch = board[i][j];
        if(ch == '#' || p.childs[ch-'a'] == null) return;
        p = p.childs[ch-'a'];
        //there is word for p;
        if(p.word != null) {
            result.add(p.word);
            p.word = null; // why? -> result has to have distinct
        }

        board[i][j] = '#';
        if(i>0) dfs(board, i-1, j, p, result);
        if(j>0) dfs(board, i, j-1, p, result);
        if(i<board.length-1) dfs(board, i+1, j, p, result);
        if(j<board[0].length -1) dfs(board, i, j+1, p, result);
        board[i][j] = ch;
    }

    private TrieNode buildTrie(String [] words) {
        TrieNode root = new TrieNode();

        for(String w: words) {
            TrieNode p = root;
            for(char c : w.toCharArray()) {
                int i = c -'a';
                if(p.childs[i] == null) {
                    p.childs[i] = new TrieNode();
                }
                p = p.childs[i];
            }
            p.word = w;
        }
        return root;
    }
}