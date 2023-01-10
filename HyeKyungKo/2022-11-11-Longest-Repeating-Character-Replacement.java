
//2022.11.11
//Time Complexity: O(n)
//Space Complexity: O(1)  <-- alphabet size 26.
class Solution {
    public int characterReplacement(String s, int k) {
        if(s == null || s.length() == 0){
            return 0;
        }

        int longestSize = 0;
        int left = 0;
        //int right = 0;
        int maxRepeatN = 0;
        int[] alphabet = new int[26];
        int currSize, diff;
        
        for(int right = 0; right < s.length(); right++){
            alphabet[s.charAt(right) - 'A']++;
            //maximum repeated number so far
            maxRepeatN = Math.max(maxRepeatN, alphabet[s.charAt(right) - 'A']);
            currSize = right - left + 1;
            diff = currSize - maxRepeatN;
            if(diff > k){
                alphabet[s.charAt(left) - 'A']--;
                left++;
            }
            //longest repeating character replacement
            longestSize = Math.max(longestSize, right - left + 1);
        }

        return longestSize;
    }
}