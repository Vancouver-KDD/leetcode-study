//Time Complexity : O(26N)= O(N) because we iterate the string of length N maximum uniqueCharNum times
//Space Complexity : O(1) because we use constant extra space of size 26 (countCharMap)

import java.util.Arrays;

class Solution {
    public int longestSubstring(String s, int k) {
        int maxLength = 0;

        if(s.length() < k) {
            return maxLength;
        }

        int uniqueCharNum = getUniqueCharNum(s);
        int countCharMap[] = new int[26];

        for(int i = 1; i <= uniqueCharNum; i++) {
        //reset countChar
        Arrays.fill(countCharMap,0);

        //reset helper variables
        int windowStart = 0;
        int windowEnd = 0;
        int index = 0;
        int currUniqueCharNum = 0;
        int charCountAtLeastK=0;

        while(windowEnd < s.length()) {
            //expand sliding window
            if(currUniqueCharNum <= i) {
                index = s.charAt(windowEnd) - 'a';
                if(countCharMap[index] == 0) {
                    currUniqueCharNum++;
                }
                countCharMap[index]++;
                if(countCharMap[index] == k) {
                    charCountAtLeastK++;
                }
                windowEnd++;

            }
            //shrink sliding window
            else {
                index = s.charAt(windowStart) - 'a';
                if(countCharMap[index] == k) {
                    charCountAtLeastK--;
                }
                countCharMap[index]--;
                if(countCharMap[index] == 0) {
                    currUniqueCharNum--;
                }
                windowStart++;
            }
            if(currUniqueCharNum == i && currUniqueCharNum == charCountAtLeastK) {
                maxLength = Math.max(maxLength, (windowEnd - windowStart));
            }
   
        }    

        }


        return maxLength;  
    }

    public int getUniqueCharNum(String s) {
        int num = 0;
        boolean[] alphabet = new boolean[26];

        for(int i = 0; i < s.length(); i++) {
            if(!alphabet[s.charAt(i) - 'a']) {
                alphabet[s.charAt(i) - 'a'] = true;
                num++;
            }
        }

        return num;
    }
}