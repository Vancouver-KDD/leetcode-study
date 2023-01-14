import java.util.*;

class Solution {
    public boolean isAnagram(String s, String t) {
        //map에 넣어서 각자 갯수 체크하기 -> not efficiend in terms of time complexity
        //map이 아니라 int[] count = new int[26]; using ASCII code
        //count[s.charAt(i)-'a']++;
        //count[s.charAt(i)-'a']--;
        Map<Character, Integer> map = new HashMap<>();
        int len = s.length();
        if(len != t.length()) return false;
        for(int i=0;i<len;i++) {  //-> O(N)
            char first = s.charAt(i);
            char second = t.charAt(i);
            map.put(first, map.getOrDefault(first, 0)+1);
            map.put(second, map.getOrDefault(second, 0)-1);
        }
        for(char key:map.keySet()) { //->O(1)
            if(map.get(key) != 0) return false;
        }
        return true;
    }
}