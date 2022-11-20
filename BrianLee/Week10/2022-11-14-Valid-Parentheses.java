class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        int start = 0;
        int end = s.length()-1;

        while(start < end) {
            while(start < s.length() && !isValid(s.charAt(start))) start++;
            while(end > -1 && !isValid(s.charAt(end))) end--;
            if(start >= end) return true;
            if(s.charAt(start) != s.charAt(end)) return false;
            start++;
            end--;
        }
        return true;
    }

    private boolean isValid(char c) {
        if('a' <= c && c <= 'z') return true;
        if('A' <= c && c <= 'Z') return true;
        if('0' <= c && c <= '9') return true;
        return false;
    }
}