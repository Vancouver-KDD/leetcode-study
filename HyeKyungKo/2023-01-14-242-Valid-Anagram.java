//limitation: s, t are null
// Input: s = "anagram", t = "nagaram"  , output: true
// Input: s = "rat", t = "car" , output: false
//2023.01.14
//Time Complexity: O(N)
//Space Complexity: O(N)
class Solution{
    public boolean isAnagram(String s, String t){
        if( s == null || s.length() == 0 || t == null || t.length() == 0){
            return false;
        }

        if(s.length() != t.length()){
            return false;
        }

        //In case of first input: s = "anagram", t = "nagaram"
        //map: (a,3), (n,1), (g,1), (r,1), (m,1)

        HashMap<Character, Integer> anagramMap = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            /*
            if(anagramMap.containsKey(ch)){
                anagramMap.put(ch, anagramMap.get(ch) + 1);
            }else{
                anagramMap.put(ch, 1);
            }*/
            anagramMap.put(ch, anagramMap.getOrDefault(ch, 0)+1);
        }

        //t = "nagaram" , map: (a,3), (n,1), (g,1), (r,1), (m,1)
        // n: (n,1)removed => (a,3), (g,1), (r,1), (m,1)
        // a: (a,3-1) => (a,2), (g,1), (r,1), (m,1)
        // g: (g,1)removed => (a,2), (r,1), (m,1)
        // a: (a,2-1) => (a,1), (r,1), (m,1)
        // r: (r,1)removed => (a,1),  (m,1)
        // a: (a,1)removed => (m,1)
        // m: (m,1)removed 
        for(int i = 0; i < t.length(); i++){
            char ch = t.charAt(i);
            if(anagramMap.containsKey(ch)){
                int value = anagramMap.get(ch);
                value--;
                if(value > 0){
                    anagramMap.put(ch, value);
                }else{
                    anagramMap.remove(ch);
                }

            }else{
                return false;
            }
        }

        return true;
    }
}

//2022.12.05
//Time Complexity: O(N)
//Space Complexity: O(1)
/*
class Solution{
    public boolean isAnagram(String s, String t){
        if( s == null || t == null || s.length() == 0 || t.length() == 0){
            return false;
        }

        if(s.length() != t.length()){
            return false;
        }

        HashMap<Character, Integer> charSet = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(charSet.containsKey(ch)){
                charSet.put(ch, charSet.get(ch)+1);
            }else{
                charSet.put(ch, 1);
            }

        }

        for(int i = 0; i < t.length(); i++){
            char ch = t.charAt(i);
            if(!charSet.containsKey(ch)){
                return false;
            }else{
                int count = charSet.get(ch);
                count--;
                if(count >  0){
                    charSet.put(ch, count);
                }else{
                    charSet.remove(ch);
                }
            }
        }

        //만약 위에서 s 와 t 의 length 를 비교했다면 굳이 아래처럼 체크할 필요가 없긴하다. 
        return charSet.size() == 0 ? true : false;
    }
}
*/

//2022.11.11
//time complexity: O(N), space complexity: O(1) <--  max 는 늘 26 임. 
/*
class Solution{
    public boolean isAnagram(String s, String t){

        if( s == null || t == null || s.length() == 0 || t.length() == 0){
            return false;
        }

        //if the length is different, it means that it is not anagram.
        if(s.length() != t.length()){
            return false;
        }

        HashMap<Character, Integer> map = new HashMap<>();

        for(int i = 0; i < s.length(); i++){
            if(map.containsKey(s.charAt(i))){
                map.put(s.charAt(i), map.get(s.charAt(i)) + 1);
            }else{
                map.put(s.charAt(i), 1);
            }
        }

        for(int i = 0; i < t.length(); i++){
            if(map.containsKey(t.charAt(i))){
                int count = map.get(t.charAt(i));
                if(count <= 1){ //remove the character from map
                    map.remove(t.charAt(i));
                }else{
                    map.put(t.charAt(i), count -1); 
                }
                
            }else{
                return false;
            }
        }

        return true;
    }
}
*/

//2022. 07.05
//time complexity: O(N), space complexity: O(N)
/*
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s == null || t == null || s.length() == 0 || t.length() == 0){
            return false;
        }
        
        if(s.length() != t.length()){   // size is different, not anagram
            return false;
        }
        
        HashMap<Character, Integer> anagramMap = new HashMap<>();
        
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            anagramMap.put(ch, anagramMap.getOrDefault(ch, 0)+1);
        }
        
        //remove same character from the HashMap
        for(int i = 0; i < t.length(); i++){
            char ch = t.charAt(i);
            if(!anagramMap.containsKey(ch)){ // not anagram
                return false;   
            }else{
                if(anagramMap.get(ch) <= 1){
                    anagramMap.remove(ch);
                }else{
                    anagramMap.put(ch, anagramMap.get(ch) -1);
                }
                
            }
        }
        
        if(anagramMap.size() > 0){
            return false;
        }
        
        return true;
    }
}
*/

//leetcode solution 
//Time complexity: O(N), Space complexity: O(1)  <-- table size 가 26 상수로 고정되기때문 
/*
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        
        int[] letters = new int[26];
        
        for(int i = 0; i< s.length(); i++){
            letters[s.charAt(i) - 'a']++;
            letters[t.charAt(i) - 'a']--;
        }
        
       
        //for(int i = 0; i < letters.length; i++){
        //    if(letters[i] != 0){
        //        return false;
        //    }
       // }
    
        for(int val : letters){
            if(val != 0){
                return false;
            }
        }
        
        return true;
    }
}
*/
//Input: s = "anagram", t = "nagaram" --> Output: true
//Input: s = "rat", t = "car" --> Output: false

//Time complexity: O(max(NlogN, MlogM)),   Space complexity: O(M+N) <---Wrong 
// Solution 의 설명은 다르네.  --> Space complexity: O(1) 
// In java, toCharArray() makes a copy of the string so it costs O(n) extra space, but we ignore this for complexity analysis because...
// . It is a lanaguage dependent detail, 
// . It depends on how the function is designed. For example, the function parameter types can be changed to char[]
//
/*
class Solution {
    public boolean isAnagram(String s, String t) {
        
        if(s.length() != t.length()){
            return false;
        }
        
        char[] charS = s.toCharArray();
        char[] charT = t.toCharArray();
        
        Arrays.sort(charS);
        Arrays.sort(charT);
        
        
        //String s2 = new String(charS);
        //String t2 = new String(charT);
        
        //if(s2.compareTo(t2) == 0){
        //    return true;
        //}
        
        //return false;
        
        //위 내용 대신 Arrays.equals 를 바로 쓸 수 있다. 
        return Arrays.equals(charS, charT);
    }
}
*/