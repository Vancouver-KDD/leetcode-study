class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for (String str : strs) {
            char[] arr = str.toCharArray();
            Arrays.sort(arr);
            String ordered = new String(arr);
            List<String> list = map.getOrDefault(ordered, new ArrayList<>());
            list.add(str);
            map.put(ordered, list);
        }
        return new ArrayList<>(map.values());
    }
}