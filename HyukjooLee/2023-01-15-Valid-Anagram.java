/**
 * Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 */

// anagram = 어떠한 단어의 character 를 분해해서 다른 단어로 바꾸는 놀이

// 1. using array to store the frequency of each chars in the array
class Solution {
    public boolean isAnagram(String s, String t) {
        // the length of two strings should be same
        if(s.length() != t.length()) return false;

        // create an array to store frequencies
        int[] freq = new int[26]; // 26 = the number of alphabet

        // iterate each character in 's' string
        for(int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
        }

        // same for the 't' string, but decrement freq
        for(int i = 0; i < t.length(); i++) {
            freq[t.charAt(i) - 'a']--;
        }

        // if frequency is not 0, it would be false
        for(int i : freq) {
            if(i != 0) return false;
        }
    
        return true;
    }
}

// 2. using hashmap to store the frequency of each char in a string
// and then compare the frequency of each char in the second string
class Solution {
    public boolean isAnagram(String s, String t) {
        // the length of two strings should be same
        if(s.length() != t.length()) return false;
        
        HashMap<Character, Integer> map = new HashMap<>();

        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            // if the current char is not in the map, add it with 1 time frequency
            if(!map.containsKey(c)) {
                map.put(c,1);
                // else, increment by 1 as it means the char already presented
            } else {
                map.put(c, map.get(c) + 1);
            }
        }
    

    }
}



