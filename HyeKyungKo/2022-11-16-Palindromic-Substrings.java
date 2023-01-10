//2022-11-16
//Input : "abc" -> output: 3  ("a", "b", "c")
//Input : "aaa" -> output: 6 ("a", "a", "a", "aa", "aa", "aaa")
//Time Complexity: O(N^2)
//Space Complexity: O(1)
class Solution {
    public int countSubstrings(String s) {
        if(s == null || s.length() == 0){
            return 0;
        }

        int totalNum = 0;
        for(int i = 0; i <= s.length(); i++){
            int left = i;
            int right = i;
            //check odd case
            while(left >= 0 && right <= (s.length()-1) && s.charAt(left)==s.charAt(right)){
                totalNum++;
                left--;
                right++;
            }
            left = i;
            right = i+1;
            //check even case
            while(left >= 0 && right <= (s.length()-1) && s.charAt(left)==s.charAt(right)){
                totalNum++;
                left--;
                right++;
            }
        }
        return totalNum;
    }
}