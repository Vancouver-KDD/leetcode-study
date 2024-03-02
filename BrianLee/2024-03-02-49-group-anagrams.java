// https://leetcode.com/problems/group-anagrams/description/

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> results = new HashMap<>();
        for(String str: strs) {
            char[] chrs = str.toCharArray();
            Arrays.sort(chrs);
            String key = String.valueOf(chrs);
            if(!results.containsKey(key)) {
                results.put(key, new ArrayList<>());
            }
            results.get(key).add(str);
        }
        return new ArrayList<>(results.values());
    }
}