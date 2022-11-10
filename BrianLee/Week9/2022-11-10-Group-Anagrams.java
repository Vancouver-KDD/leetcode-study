class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> group = new HashMap<>();
        for(String str: strs) {
            char[] strArray = str.toCharArray();
            Arrays.sort(strArray);
            group.computeIfAbsent(String.valueOf(strArray), __ -> new ArrayList<>()).add(str);
        }
        return new ArrayList<>(group.values());
    }
}

