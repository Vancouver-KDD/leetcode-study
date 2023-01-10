//2022.11.11
//limitation: s, t are null
// Input: s = "anagram", t = "nagaram"  , output: true
// Input: s = "rat", t = "car" , output: false

//time complexity: O(N), space complexity: O(1) <--  max 는 늘 26 임. 
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
