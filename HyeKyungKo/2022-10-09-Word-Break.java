
//question: 1) wordDict's words have random order?  
//            ex) "leetcode" -> "code", "leet"
//        2) in case of same word, wordDict has it one time? 
//           ex) "leetcodeleet" -> ["leet", "code", "leet"] vs ["leet", "code"]
//        3) case sensitive? or S and wordDict consist of only lowercase???
//         4) wordDict has more words than substring of input s -> "leet", ["cat", "le", "leet", "dog"]
//                                
//input: "bababaa"  ["aa", "ab", "bab"] -> Output: true
//input: "leetcode" ["leet", "neet", "code"] -> output: true
//input: "bababcaa" ["aa", "ab","ba","babab", "bababcaa"] -> output: true

//2022.10.09
//Time Complexity : O(n^3) O of N cubed ( for loop * for loop * substring)
//Space Complexity: O(n) <-- boolean array
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        
        if(s == null || s.length() == 0 || wordDict == null || wordDict.size()== 0){
            return false;
        }
        
        HashSet<String> wordDictSet = new HashSet<>(wordDict);
        
        boolean[] wordBreak = new boolean[s.length()+1];
        wordBreak[0] = true;
        
        for(int i = 1; i <= s.length(); i++){
            for(int j = 0; j < i; j++){
                if(wordBreak[j] == true && wordDictSet.contains(s.substring(j, i))){
                    wordBreak[i] = true;
                    break;
                }
            }
        }
        
        return wordBreak[s.length()];
    }
}