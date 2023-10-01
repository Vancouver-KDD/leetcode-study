class Solution {
    public int longestSubstring(String s, int k) {
    if(s.length() < k) return 0; // base case
		int[] count = new int[26];
		for(int i = 0; i < s.length(); i++) count[s.charAt(i)-'a']++; // count the frequency of each character
		for(int i = 0; i < s.length(); i++) {
			if(count[s.charAt(i)-'a'] >= k) continue;
			int j = i + 1;
			while(j < s.length() && count[s.charAt(j)-'a'] < k) j++;
            // if the frequency of the character is less than k, then we need to split the string into two parts
            // and recursively call the function to find the longest substring
            // divide and conquer
			return Math.max(longestSubstring(s.substring(0, i), k), longestSubstring(s.substring(j), k));
		}
		return s.length();
        
    }
}