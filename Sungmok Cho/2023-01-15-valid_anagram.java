// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false
 

// Constraints:

// 1 <= s.length, t.length <= 5 * 104
// s and t consist of lowercase English letters.

class Solution {
    public boolean isAnagram(String s, String t) {
        char sArray [] = s.toCharArray();
        char tArray [] = t.toCharArray();

        Arrays.sort(sArray);
        Arrays.sort(tArray);
        
        boolean check = false;
        
        for(int i = 0; i < t.length(); i++) {
            if(sArray[i] == tArray[i]) {
                check = true;
            } else {
                check = false;
                break;
            }
        }

        return check;
    }
}