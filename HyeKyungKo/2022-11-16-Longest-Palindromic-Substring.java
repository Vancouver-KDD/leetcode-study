//2022.11.16
//아래 방법이 brute-force 방법인줄 알고 풀었는데 아니였네. ---> Expand Around Center 방법이라네...
//Input : "babad" -> Output: 
//Time complexity: O(n^2)
//Space Complexity: O(1)
class Solution{
    public String longestPalindrome(String s){
        if(s == null || s.length() <= 1){
            return s;
        }

        String longest = ""; 
        for(int i = 0; i < s.length(); i++){
            int left = i-1;
            int right = i+1;
            int currSize1 = 0;
            while(left >= 0 && right <= s.length()-1 && s.charAt(left)== s.charAt(right)){
                left--;
                right++;
            }
            //palindrome start position: left+1, palindrome end position:right-1 
            currSize1 = right - left -1;
            if(longest.length() < currSize1){
                longest = s.substring(left+1,right);
            }
            int currSize2 = 0;
            left = i;
            right = i+1;
            while(left >= 0 && right <= s.length()-1 && s.charAt(left) == s.charAt(right)){
                left--;
                right++;
            }
            //palindrome start position: left+1, palindrome end position:right-1
            currSize2 = right - left -1;
            if(longest.length() < currSize2){
                longest = s.substring(left+1, right);
            }
        }

        return longest;
    }
}

/*
class Solution {
    //Solution from leetcode
    public String longestPalindrome(String s) {      
        
        //check if no data
        if(s == null || s.length() < 0){
            return "";
        }
        
        int start = 0;
        int end = 0;
        int longestLength = 1;
        for(int i = 0; i < s.length(); i++){
            int length1 = expandPalindromeString(s, i, i);
            int length2 = expandPalindromeString(s, i, i+1);
            int longLength = Math.max(length1, length2);
            if(longestLength < longLength){
                longestLength = longLength;
                start = i - (longLength -1) /2;
                end = i + longLength /2;           
            }
        }
        return s.substring(start, end+1);
        
    }
    
    int expandPalindromeString(String s, int index1, int index2){
        int left = index1;
        int right = index2;
        
        while( left >=0 && right < s.length() && (s.charAt(left) == s.charAt(right))){
            
            left--;
            right++;
        }
        
        return (right - left -1);
        
    }
}
*/  