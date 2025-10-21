class Solution {
    public int[] productExceptSelf(int[] nums) {
        /*
            Time Complexity: O(n)
            Space Complexity: O(n)
         */
        int productOfLeft = 1;
        int productOfRight = 1;

        int[] result = new int[nums.length];

        // store products of all elements to the left of each index
        for (int i = 0; i < result.length; i++) {
            result[i] = productOfLeft;
            productOfLeft *= nums[i];
        }

        // multiply each result[i] by the product of all elements to the right of index i
        for (int i = result.length - 1; i >= 0; i--) {
            result[i] *= productOfRight;
            productOfRight *= nums[i];

        }

        return result;
    }
}