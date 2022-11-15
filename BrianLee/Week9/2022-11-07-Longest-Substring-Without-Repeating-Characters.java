class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int max = 0;
        int start = 0;
        for(int end = 0; end < s.length(); end++) {
            while(set.contains(s.charAt(end))) {
                set.remove(s.charAt(start++));
            }
            set.add(s.charAt(end));
            max = Math.max(max, set.size());
        }
        return max;
    }
}