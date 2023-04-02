class Solution {
    int count = 1;
    //when it comes to palindrome -> think about benchmark
    public int countSubstrings(String s) {
        int len = s.length();
        for(int i=0; i< len-1; i++){
            checkPalindrome(s,i,i);    //odd
            checkPalindrome(s,i,i+1);  //even
        }
        return count;  
    }

    private void checkPalindrome(String s, int i, int j) {
        while(i>=0 && j<s.length() && s.charAt(i)==s.charAt(j)){   
            count++;    
            i--;    
            j++;   
        }
    }
}
//O(N^2)