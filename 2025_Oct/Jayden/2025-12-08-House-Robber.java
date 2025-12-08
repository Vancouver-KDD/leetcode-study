class Solution {
    /**
        Time Complexity: O(n)
        Space Complexity: O(1)
     */
    public int rob(int[] nums) {
        int rob1 = 0;
        int rob2 = 0;

        for (int num : nums) {
            // Option 1: Rob current house + best from two houses ago (rob1)
            // Option 2: Don't rob current house -> keep best from previous (rob2)
            int temp = Math.max(num + rob1, rob2); // ex. [2,1,1,2]: [0, 2] -> [2, 2] -> [2, 3] -> [3, 4]
            rob1 = rob2;
            rob2 = temp;
        }

        return rob2;

    }
}