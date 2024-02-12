https://leetcode.com/problems/unique-binary-search-trees/description/

class Solution {
    public int numTrees(int n) {
        int[] counts = new int[n+1];
        counts[0] = 1;
        counts[1] = 1;

        for(int i = 2; i < n+1; i++) {
            int total = 0;
            for(int j = 1; j < i+1; j++) {
                total += counts[j-1] * counts[i-j];
            }
            counts[i] = total;
        }
        return counts[n];
    }
}