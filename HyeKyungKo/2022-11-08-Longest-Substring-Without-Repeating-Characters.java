//leetcode - solution #2
//time complexity: O(n) , space complexity : O(m) : m is the number of character set.(최대 128)
//input : abcabcbb -> output: 3 ( abc)
//input : pwwkew -> output : 3 (wke)
//input: abba -> output: 2 ( ab or ba)

//2022.11.08
public class Solution{
    public int lengthOfLongestSubstring(String s){
        if( s == null || s.length() == 0){
            return 0;
        }

        HashMap<Character, Integer> charMap = new HashMap<>();
        int start = 0;
        int longest = 1;
        for(int i = 0; i < s.length(); i++){
            if(!charMap.containsKey(s.charAt(i))){
                charMap.put(s.charAt(i), i); //add new data
            }else{//repeating character
                int index = charMap.get(s.charAt(i));
                if(index >= start){ // it means 's.charAt(i)' is a repeating character between start and [i] --> update the 'start'
                    start = charMap.get(s.charAt(i)) + 1;
                }
                charMap.put(s.charAt(i), i); //update 'value'
            }
            longest = Math.max(i+1 - start, longest);
        }

        return longest;
    }
}
//-------------------------------------------------
/*
public class Solution {
    public int lengthOfLongestSubstring(String s) {
       
        if( s == null){
            return 0;
        }
        
        HashMap<Character, Integer> map = new HashMap<>();
        int longest = 0;    
        int current = 0;
        int startPos = 0;
        
        for(int i = 0; i < s.length(); i++){
            if(!map.containsKey(s.charAt(i)) || map.get(s.charAt(i)) < startPos){
                current++;
            }else{
                current = i - map.get(s.charAt(i));
                startPos = map.get(s.charAt(i)) + 1;
                
            }
            
            map.put(s.charAt(i), i);
            if(longest < current){
                    longest = current;
            }
        }
               
        return longest;
    }
}
 */       
        
/*
//Time complexity: O(n)
//Space Complexity: O(m) <- m 은 128 로 일정 
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        Integer[] characters = new Integer[128];
        int length = 0;
        
        int left=0; 
        int right = 0;
        while(right < s.length()){
            
            char ch = s.charAt(right);
            
            //if(characters[ch] != null && (characters[ch] >= left && characters[ch] < right)){
            if(characters[ch] != null && (characters[ch] >= left)){
                left = characters[ch]+1;
            }
            length = Math.max(length, right - left + 1);
            characters[ch] = right;
            
            right++;
        }
        
        return length;
    }
}
*/  
//leetcode - solution #1
/*
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), ans = 0;
        Map<Character, Integer> map = new HashMap<>(); // current index of character
        // try to extend the range [i, j]
        for (int j = 0, i = 0; j < n; j++) {
            if (map.containsKey(s.charAt(j))) {
                i = Math.max(map.get(s.charAt(j)), i);

            }
            ans = Math.max(ans, j - i +1 );
            map.put(s.charAt(j), j +1);
        }
        return ans;
    }
}
*/
//My Solution 
// time complexity : O(n) ,  Space complexity: O(m) , m is the number of charset.
/*
class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        if(s == null || s.length() == 0){
            return 0;
        }
        
        int longestSize = 0;
        Map<Character, Integer> map = new HashMap<>();
        int startPos= 0;
        int repeatPos = 0;
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(map.containsKey(ch)){
                longestSize = Math.max(longestSize, map.size());
                
                repeatPos = map.get(ch);
                for(int j = startPos; j <= repeatPos; j++){
                    map.remove(s.charAt(j));
                }
                startPos = repeatPos+1;
            }            
            map.put(ch, i);            
        }
        
        return Math.max(longestSize, map.size());
    }
}
*/