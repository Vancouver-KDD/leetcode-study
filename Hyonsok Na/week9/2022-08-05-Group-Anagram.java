class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap();
        for(int i = 0; i<strs.length; i++) {
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String s = new String(chars);
            if(map.containsKey(s)) {
                List<String> list = map.get(s);
                list.add(strs[i]);
                map.replace(s, list);
            } else {
                List<String> list = new ArrayList();
                list.add(strs[i]);
                map.put(s, list);
            }
        }
        return new ArrayList(map.values());
    }
}