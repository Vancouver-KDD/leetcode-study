//leetcode - solution #2
//time complexity: O(n) , space complexity : O(m) : m is the number of character set.(최대 128)
//input: abbca -> output: 3 (bca)
//input : abcabcbb -> output: 3 ( abc)
//input : pwwkew -> output : 3 (wke)
//input: abba -> output: 2 ( ab or ba)

//2023-01-25
//Similar question: 1695. Maximum Erasure Value
//[idea] : Using HashMap- <key, value> = <character, position>
//           if there is same character, move starting point of the substring
//                      Also, compare the length of longest substring 
//time complexity: O(n) , space complexity : O(m) : m is the number of character set.(최대 128)
public class Solution{
    public int lengthOfLongestSubstring(String s){
        if(s == null || s.length() == 0){
            return 0;
        }

        HashMap<Character, Integer> charMap = new HashMap<>();
        int longestLength = 0;
        int start = 0;
        //input : abcabcbb
        //Map : (a,0),(b,1),(c,2), (a,3), (b,4),(c,5),(b,6),(b,7)
        //current: 1    2     3      3      3    3      2     1
        //longest: 1    2     3      3      3    3      3     3
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(!charMap.containsKey(ch)){
                charMap.put(ch, i);//add new data
            }else{

                start = Math.max(start, charMap.get(ch) + 1);
                charMap.put(ch, i); //update
            }
            int currentLength = i - start + 1;
            longestLength = Math.max(longestLength, currentLength);
        }

        return longestLength;
    }
}

//2022-12-05
/*
1) HashMap(Integer, Integer) :key는 alphabet, value 는 index 인 map 만들기 
2) start = 0, longest = 0 으로 두기
2) string 길이 (0~ length-1) 만큼 돌면서 map 에 없으면 char 넣고, longest length 값 증가
3) 만약 map 에 이미 있다면
    3-1) map에 저장된 index >= start 이면, 반복된 것이니, start = index+1 로 update
         map내 index 도 현재 i 값으로 update
    3-2) map에 저장된 index < start 이면, 현재 체크하는 substring 범주내의 값이 아니니 start는 유지하고
    3-3) map 내 index 를 i 값으로 update  
*/
//Time complexity: O(N) <- N 은 string 길이 
//Space Complexity: O(M) <- M 은 the number of character set
/*
public class Solution{
    public int lengthOfLongestSubstring(String s){
        if( s == null || s.length() == 0){
            return 0;
        }

        HashMap<Character, Integer> map = new HashMap<>();
        int start = 0;
        int longest = 0;
        for(int end = 0; end < s.length(); end++){
            char ch = s.charAt(end);
            if(!map.containsKey(ch)){
                map.put(ch, end);
            }else{
                int index = map.get(ch);
                if(index >= start){ // repeat 
                    start = index +1; 
                }
                //index update
                map.put(ch, end);
            }
            int subStringSize = end - start +1; 
            longest = Math.max(longest, subStringSize);
        }
        return longest;
    }
}
*/
//2022.11.08
/*
public class Solution{
    public int lengthOfLongestSubstring(String s){
        if( s == null || s.length() == 0){
            return 0;
        }

        HashMap<Character, Integer> charMap = new HashMap<>();
        int start = 0; 
        int longest = 1;
        for(int end = 0; end < s.length(); end++){
            char key = s.charAt(end);
            if(!charMap.containsKey(key)){
                charMap.put(key, end); //add new data
            }else{ // repeated character
                start = Math.max(charMap.get(key) +1, start); //update start position
                charMap.put(key, end); //update index
            }
            int currSize = end - start +1;
            longest = Math.max(currSize, longest);
        }

        return longest;
    }
}
*/ 
/*
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
*/
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