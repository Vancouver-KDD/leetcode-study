/* https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
 * 
 * ## Description 
 * Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater * than or equal to k. If no such substring exists, return 0.
 * 
 * 
 */

public int longestSubstring(String s, int k) {
    //Get the number of unique char from 's'
    int maxUnqiueCharCount =  getUniqueCharCount(s);
    //It will store how many times each char is repeated in 's'
    int [] freqMap = new int [26];
    int result = 0;
    
    //Traverse by the number of char is allowed in substring (1 to number of unique char we got above)
    for (int currentUniqueChar = 1;  currentUniqueChar <= maxUnqiueCharCount; currentUniqueChar++) {

        //Each traversal, we need to reset the frequency map, counters, pointers 
        Arrays.fill(freqMap, 0);
        int uniqueCount = 0, countAtLeastK = 0, windowStart  = 0, windowEnd = 0;   

        // loop through until the end pointer reaches to the end.         
        while (windowEnd < s.length()) {
            
            //Expanding the window when the unique char count in substring has not exceeded the allowed number of unique char we are checking. 
            if (uniqueCount <= currentUniqueChar) {
                int idx = s.charAt(windowEnd) - 'a';
                //Check if the char is new in frequency map, then we need to count 
                if (freqMap[idx] == 0) {
                    uniqueCount++;
                }
                //Update the frequency of char 
                freqMap[idx]++; 
                
                //If the frequency is same as k, update the counter for k 
                if (freqMap[idx] == k) {
                    countAtLeastK++;
                }
                //move the end pointer to the right as expanding the window 
                windowEnd++;
            } else { //Shrinking the window when the unique char count in substring has exceeded the allowed number. 
                int idx = s.charAt(windowStart) - 'a';

                //As shrinking the window, we need to reset the counters related to the chars that are being excluded
                if (freqMap[idx] == k) {
                    countAtLeastK--;
                }
                freqMap[idx]--;
                if (freqMap[idx] == 0) {
                    uniqueCount--;
                }
                //Move the start pointer to the right as shrinking the window 
                windowStart++;
            }
            
            //Each iteration, we need to check two things 
            // 1. if the unique char in substring is the same as the allowed number of unique char we are checking in this iteration. 
            // 2. if all the unique chars in substrings are repeated at least k times.  
            if (uniqueCount == currentUniqueChar && uniqueCount == countAtLeastK) {
                //Update the result to maximum value 
                result = Math.max(windowEnd - windowStart, result);
            }
        }
        
    }
    
    return result;
}


private int getUniqueCharCount(String s) {
    //boolean arrays are set to false by default. 
    //set the size as the number of alphabet
    boolean [] chars = new boolean [26];
    int uniqueCount = 0;
    
    for (char ch : s.toCharArray()) {
        //getting indices using ASCII 
        int idx  = ch - 'a';
        if (!chars[idx]) {
            uniqueCount++;
            //set to true so the same chars not be counted. 
            chars[idx] = true; 
        }
    }
    
    return uniqueCount;
}
