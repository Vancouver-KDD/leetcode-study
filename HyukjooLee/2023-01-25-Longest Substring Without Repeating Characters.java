/**
 * Given a string s, find the length of the longest substring without repeating characters.
 * e.g.
 * Input: s = "abcabcbb"  => The answer is "abc", with the length of 3.
 */

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int resultLength = 0;
        Map<Character, Integer> map = new HashMap<>();
        int i = 0; s
        for(int j = 0; j < s.length(); j++) {
            if(map.containKey(s.charAt(j))) {
                i = Math.max(i, charMap.get(s.charAt(j)) + 1);
            }
            map.put(s.charAt(j), j);
            resultLength = Math.max(resultLength, j - i + 1);
        }   
        return resultLength;
    }
}