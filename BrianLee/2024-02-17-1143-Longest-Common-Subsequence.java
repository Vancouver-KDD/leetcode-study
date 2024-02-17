https://leetcode.com/problems/longest-common-subsequence/

class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        //   a b c d e
        // a 3         0
        // c   2 2     0
        // e       1 1 0
        //   0 0 0 0 0 0
        int[][] memory = new int[text1.length()+1][text2.length()+1];

        for(int i = text1.length()-1; i >= 0; i--) {
            for(int j = text2.length()-1; j >= 0; j--) {
                if(text1.charAt(i) == text2.charAt(j)) {
                    memory[i][j] += 1+ memory[i+1][j+1];
                } else {
                    memory[i][j] = Math.max(memory[i+1][j], memory[i][j+1]);
                }
            }
        }

        return memory[0][0];
    }
}