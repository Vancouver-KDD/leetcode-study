class LengthOfLongestSubstring {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        int i = 0, max = 0;
        for (int j = 0; j < s.length(); j++) {
            char right = s.charAt(j);
            if (!map.containsKey(right) || map.get(right) < i) {
                map.put(right, j);
                max = Math.max(max, j - i + 1);
            } else {
                i = map.get(right) + 1;
                map.put(right, j);
            }
        }
        return max;
        // i 2 j 6
    }
}