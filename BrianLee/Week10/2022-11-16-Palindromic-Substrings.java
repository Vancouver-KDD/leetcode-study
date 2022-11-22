class Solution {
    public int countSubstrings(String s) {
        int result = 0;
        for(int i = 0 ; i < s.length(); i++) {
            result += getPalindromic(s,i,i);
            if(i+1 < s.length()) result += getPalindromic(s,i,i+1);
        }
        return result;
    }

    private int getPalindromic(String s, int i, int j) {
        int start = i;
        int end = j;
        int count = 0;

        while(start >= 0 && end < s.length()) {
            if(s.charAt(start--) == s.charAt(end++)) count++;
            else break;
        }
        return count;
    }
}