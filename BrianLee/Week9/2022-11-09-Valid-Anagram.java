class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        Arrays.sort(sChars);
        Arrays.sort(tChars);

        for(int i = 0; i < sChars.length; i++) {
            if(sChars[i] != tChars[i]) return false;
        }

        return true;
    }
}