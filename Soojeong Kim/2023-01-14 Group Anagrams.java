import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        HashMap<String, List<String>> map = new HashMap<>();
        int len = strs.length;

        for(int i = 0; i<len;i++) {
            char [] temp = strs[i].toCharArray();
            Arrays.sort(temp);
            String sorted = String.valueOf(temp);

            if(map.containsKey(sorted)) {
                map.get(sorted).add(strs[i]);
            }else {
                List<String> list= new ArrayList<>();
                list.add(strs[i]);
                map.put(sorted, list);
            }
        }

        for(String key:map.keySet()) {
            result.add(map.get(key));
        }
        return result;
    }
}