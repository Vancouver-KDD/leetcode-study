https://leetcode.com/problems/word-break/

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {

        Set<String> words = new HashSet<>(wordDict);
        boolean[] mem = new boolean[s.length()];
        for(int i = 0; i < s.length(); i++) mem[i] = true;

        wordBreak(s, words, 0, mem);

        return mem[0];
    }

    public boolean wordBreak(String s, Set<String> wordDict, int current, boolean[] mem) {
        if(current == s.length()) return true;
        if(mem[current] == false) return false;

        for(int j = current+1; j <= s.length(); j++) {
            String word = s.substring(current, j);
            if(wordDict.contains(word)) {
                if(wordBreak(s, wordDict, j, mem)) {
                    return true;
                }
            }
        }

        mem[current] = false;
        return false;
    }
}