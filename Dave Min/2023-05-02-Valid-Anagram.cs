public class Solution {
    public bool IsAnagram(string s, string t) {
        int[] sLetters = new int[26];
        int[] tLetters = new int[26];
        //To insert all letters of string s into sLetters 
        //based on their nemerical value from the letter
        // (int)'c' - (int)'a' = 2 
        // (int)'b' - (int)'a' = 1
        for(int i=0; i< s.Length ;i++){
            int num = (int)s[i]-(int)'a';
            sLetters[num]++;
        }
        //To insert all letters of string t into sLetters 
        //based on their nemerical value from the letter
        for(int i=0; i< t.Length ;i++){
            int num = (int)t[i]-(int)'a';
            tLetters[num]++;
        }     
        //To compare  sLetters with tLetters
        //If all int value(the number of each letter) are the same, then True will be returned.
        //Otherwise, False will be return once it's found.
        for(int i=0; i<26 ;i++){
            if(sLetters[i] != tLetters[i]) return false;
        } 
        return true;
    }
}
